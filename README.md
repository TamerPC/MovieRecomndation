# Machine learning based simple movie recomendation system
## python version 3.11.10

```pip install -r requirements.txt```
### Team memebers:

Tugambayeva Aruzhan;
Lyailya Dzhumagulova;
Aitzhanov Sultan;
Vyacheslav Popov;
Tamerlan Kabdolla. 
## Main statements


### Model architecture is VAE

![alt text](https://www.mdpi.com/applsci/applsci-13-12413/article_deploy/html/images/applsci-13-12413-g001.png)

The essence of the model is to train it to find the main features from the data and form them into a vector of limited length
and restore the original data from it.
in the future we will only need the first part of the autoencoder "encoder". This process is called feature extraction.

After successful training, we will have a working encoder that will form vectors describing our films.

Using the cosine similarity or any other, we will be able to compare each film mathematically as in the KNN model.

Similar films will be located nearby in our multidimensional vector space.

(The cosine similarity will show for the same film a distance of 1 for the opposite -1, neutral 0, the more similarities between films, the closer to 1 the distance will be)

Based on this data, we will issue recommendations based on the films that the user marked as liked, as well as on the request that the user writes himself. by cosine distance, you can issue the closest to 1. 

## Data format 

I use own tokenizer for text data representation.
For example string like: "hello : – my friendOOO" would be like: [877, 1320, 1744, 9374, 11894, 2834, 672, 986, 1530, 1650, 15] in number form.

Each token has max length 2 characters. It can be longer if you want, but in our case i think 2 chars pretty enough.

## WEB page
backend written on Flask.

We have simple form where we can choose user, and write prefered genre and description for movie.

On "My films" side we can see movies which user marked as liked. And in the "Recomendations we show our recomendations from ML model"

## Motivation and Objective (Problem, Challenge)
Motivation: The goal of this project is to build a film recommendation system that provides personalized suggestions based on the user's viewing history and preferences. Traditional recommendation systems often rely on collaborative filtering or content-based filtering, but the challenge is how to combine both methods effectively, particularly in a way that scales well and maintains accuracy.

Objective: We aim to use machine learning, specifically autoencoders, to extract features from films, represent them in a lower-dimensional vector space, and compare these vectors using cosine similarity to recommend similar films.
## Related Work and Originality
Related Work: There are many approaches to film recommendation systems. Collaborative filtering, such as the one used by Netflix, leverages user-item interaction matrices to suggest films based on user preferences. Content-based filtering uses film features like genre, director, or description to make recommendations. More recently, autoencoders have been used for feature extraction, and cosine similarity has been applied to measure the closeness between films.

Originality: This project combines autoencoders for feature extraction with a custom-built tokenizer for text processing, offering a unique approach to vectorizing film descriptions. Additionally, the backend is powered by Flask, allowing for a simple user interface to interact with the model and receive real-time recommendations.

## Design Architecture

Data Collection: We gather film data including title, genre, description, director, cast, etc.

Preprocessing: Tokenization and vectorization of film descriptions using a custom tokenizer.

Encoder: An autoencoder architecture is trained to extract features and compress them into a fixed-length vector.

Recommendation Generation: The model uses cosine similarity to compare films and recommend similar ones based on the user’s viewing history.

Backend: The backend is built using Flask, which handles user requests and interacts with the trained model to generate recommendations.

## Detailed Algorithm or Functions

Encoder Model:

Input: Film data (title, description, etc.).
Process: The encoder learns to map the input data into a lower-dimensional space by minimizing reconstruction error.
Output: A fixed-length vector representing the film.

Formula for reconstruction error:![image](https://github.com/user-attachments/assets/2799ae0e-b634-4d50-be07-04f491216e36)



 Cosine Similarity:
Cosine similarity is used to compare the generated vectors of different films:


![image](https://github.com/user-attachments/assets/5fbfdfca-1876-40aa-918c-125a380f2a8e)

Recommendation Generation:

Based on the user's past whatched films, the system computes the cosine similarity of the user's film vectors with all available films in the dataset. Films with the highest similarity scores are recommended.

## Coding

You can find files with code by  this github link: https://github.com/TamerPC/MovieRecomndation

## Results and Performance Evaluation

Model Accuracy: We achieved an accuracy of 99.75% on test data.

Cosine Similarity: The cosine similarity is used to measure the closeness of films based on the encoder-generated vectors. The closer the cosine similarity value is to 1, the more similar the films are.

Real-time Recommendations: The system is able to provide accurate recommendations based on user history and film features.

Kullback-Leibler (KL) Divergence: KL Divergence was used during the training phase to measure how much the predicted distribution deviates from the actual data distribution. Minimizing KL Divergence ensures that the autoencoder's encoded features are close to the original data distribution, which improves the accuracy of the model.

Training/Testing Loss: The model’s performance during training and testing was evaluated using the loss function.

![image](https://github.com/user-attachments/assets/d7cbe1ff-e5cc-432a-bf56-946ff7724a5b)

## Conclusion

In this project, we developed a personalized film recommendation system using a machine learning approach that combines autoencoders for feature extraction and cosine similarity for similarity-based recommendations.

The encoder successfully transformed high-dimensional film data into compact, meaningful vectors, allowing us to represent films in a multidimensional vector space. By using cosine similarity, we could accurately measure the closeness between films, enabling precise and relevant recommendations.

Our model demonstrated excellent performance with a 99.75% accuracy on test data. The system was deployed on a user-friendly website, allowing users to view their liked films, select preferred genres or descriptions, and receive real-time recommendations tailored to their preferences.

## Reference

Сафронов, А. (2022, September 14). Искусственный интеллект в поиске. Как Яндекс научился применять нейронные сети, чтобы искать по смыслу, а не по словам. Хабр. https://habr.com/ru/companies/yandex/articles/314222/

Search | Kaggle. (n.d.). https://www.kaggle.com/search?q=Movie+Recommendation+System

## Roles of Members
Team Lead / Data Scientist / Senior ML Developer: Tamerlan Kabdolla -  

Senior Data Miner and preparation / Data Analytic: Aitzhanov Sultan

Senior Data Scientist / Data Miner: Vyacheslav Popov 

Senior Web Developer / Data Miner: Tugambayeva Aruzhan

Senior Project Manager / Data Miner: 
Lyailya Dzhumagulova 

## Bonus

You Tube link

![image](https://github.com/user-attachments/assets/5ff9da3f-3480-469e-986a-902c82df2aa2)


