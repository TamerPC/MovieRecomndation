# Machine learning based simple movie recomendation system
## python version 3.11.10

```pip install -r requirements.txt```

## Main statements

### Model architecture is VAE

![alt text](https://www.mdpi.com/applsci/applsci-13-12413/article_deploy/html/images/applsci-13-12413-g001.png)

The essence of the model is to train it to find the main features from the data and form them into a vector of limited length
and restore the original data from it.
in the future we will only need the first part of the autoencoder "encoder". This process is called feature extraction.

After successful training, we will have a working encoder that will form vectors describing our films.

Using the cosine distance or any other, we will be able to compare each film mathematically as in the KNN model.

Similar films will be located nearby in our multidimensional vector space.

(The cosine distance will show for the same film a distance of 1 for the opposite -1, neutral 0, the more similarities between films, the closer to one the distance will be)

Based on this data, we will issue recommendations based on the films that the user marked as liked, as well as on the request that the user writes himself. by cosine distance, you can issue the closest to 1. 