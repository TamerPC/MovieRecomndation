import json

with open('data/final_dataset.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

import numpy as np

dataset = []

for key in data:
  dataset.append(np.array(data[key][7]))

dataset.append(np.array([0.0]*964))

dataset = np.array(dataset)
dataset = dataset /11990

train_set = dataset[:10]
test_set = dataset[3000:]

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Input, Dense, Lambda, Reshape, Dropout, BatchNormalization, Flatten
import tensorflow.keras.backend as K
import tensorflow as tf

input_size = 964
latent_dim = 128
batch_size = 100

def dropout_and_batchnorm(x):
  return Dropout(0.3)(BatchNormalization()(x))

#Encoder
input_encoder = Input(batch_shape=(batch_size, input_size))
x = Flatten()(input_encoder)
x = Dense(482, activation='relu')(x)
x = dropout_and_batchnorm(x)
x = Dense(241, activation='relu')(x)
x = dropout_and_batchnorm(x)
x = Dense(128, activation='relu')(x)
x = dropout_and_batchnorm(x)

z_mean = Dense(latent_dim)(x)
z_log_var = Dense(latent_dim)(x)

def noiser(args):
  global z_mean, z_log_var
  z_mean, z_log_var = args
  N = tf.random.normal(shape=(batch_size, latent_dim), mean=0., stddev=1.0)
  return tf.exp(z_log_var/2) * N + z_mean

#hidden vector
h = Lambda(noiser, output_shape=(latent_dim,))([z_mean, z_log_var])

#Decoder
input_decoder = Input(shape=(latent_dim,))
d = Dense(128, activation='relu')(input_decoder)
d = dropout_and_batchnorm(d)
d = Dense(241, activation='relu')(d)
d = dropout_and_batchnorm(d)
d = Dense(482, activation='relu')(d)
d = dropout_and_batchnorm(d)
decoded = Dense(input_size, activation='sigmoid')(d)

encoder = keras.Model(input_encoder, h, name="encoder")
decoder = keras.Model(input_decoder, decoded, name="decoder")
vae = keras.Model(input_encoder, decoder(encoder(input_encoder)), name="vae")

def vae_loss(x, y):
  batch_size_current = tf.shape(x)[0]
  x = tf.reshape(x, shape=(batch_size_current, input_size))
  y = tf.reshape(y, shape=(batch_size_current, input_size))
  loss = K.sum(K.square(x-y), axis=-1)
  kl_loss = -0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1) #Kullback-Leibler divergence
  return loss + kl_loss

vae.compile(optimizer='adam', loss=vae_loss)

def train_model():
  history = vae.fit(train_set, train_set, epochs=100, batch_size=batch_size, shuffle=True, validation_split=0.2)

  plt.subplot(1, 2, 1)
  plt.plot(history.history['loss'], label='Training Loss')
  plt.plot(history.history['val_loss'], label='Validation Loss')
  plt.title('Training and Validation Loss')
  plt.xlabel('Epochs')
  plt.ylabel('Loss')
  plt.legend()
  plt.show()


def predict(data):
  vae.load_weights("dl_model/vae.h5")
  encoder.load_weights("dl_model/encoder.h5")

  data = np.array(data)
  data = np.reshape(data, (1, 964)).astype(float)
  return encoder.predict(np.reshape(data, (1, 964)).astype(float))
  # return vae.predict(data)


def calc_accuracy(train=True):
  res = []

  if train:
    for i in train_set:
      res.append(predict(i))
  else:
    for i in test_set:
      res.append(predict(i))

  accuracy = 0
  for i in range(0,len(res)-1):
    threshold = 0.01
    accuracy += round(np.mean((res[i]-test_set[i])<threshold))

  print(res)

  return accuracy/len(res)