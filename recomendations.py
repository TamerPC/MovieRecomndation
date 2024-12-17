import numpy as np
from scipy.spatial.distance import cosine
import json

with open('test.json', 'r', encoding='utf-8') as file:
    vectors = json.load(file)

# Определенный элемент, с которым сравниваем
target_key = "120"
target_vector = vectors[target_key]

# Считаем косинусное расстояние для всех остальных векторов
cosine_distances = []
for key, vector in vectors.items():
    if key != target_key:  # Исключаем целевой элемент
        distance = cosine(target_vector, vector)  # Косинусное расстояние
        cosine_distances.append((key, distance))

# Сортируем по убыванию косинусного сходства (т.е., по возрастанию расстояния)
cosine_distances.sort(key=lambda x: x[1])

# Берём топ-100 элементов
top_10 = cosine_distances[:10]

# Выводим результат
for key, distance in top_10:
    print(f"Key: {key}, Cosine Distance: {distance}")