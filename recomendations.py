import numpy as np
from scipy.spatial.distance import cosine
import json

def recommend(target="0", target_vec=[]):
    with open('data/vectors_for_rec.json', 'r', encoding='utf-8') as file:
        vectors = json.load(file)

    target_key = target
    target_vector = vectors[target_key]

    if target_vec != []:
        target_vector = target_vec

    cosine_distances = []
    for key, vector in vectors.items():
        if key != target_key:
            distance = cosine(target_vector, vector)
            cosine_distances.append((key, distance))

    cosine_distances.sort(key=lambda x: x[1])

    top_10 = cosine_distances[:10]

    res = []
    for key, distance in top_10:
        res.append(key)

    return res