from flask import Flask, render_template, request, redirect, url_for
import json
from tokenizer.tokenizer import Tokenizer
from recomendations import recommend
from dl_model.model import predict

app = Flask(__name__)

with open("data/for_web.json", 'r', encoding='utf-8') as file:
    filmoteka = json.load(file)

with open("users.json", 'r', encoding='utf-8') as file:
    users = json.load(file)

with open("data/genres_select.json", 'r', encoding='utf-8') as file:
    genres_json = json.load(file)
    genres = []
    for key, item in genres_json.items():
        genres.append([key, item])


@app.route('/', methods=['GET', 'POST'])
def index():
    user = "1"
    recomended_films = []

    if request.method == 'POST':
        describe = request.form.get("describe")
        genre = request.form.get("genre")
        user = request.form.get("user")

        recomended_films = []
        for rec in recommend(target_vec=format_vector(describe, genre)):
            recomended_films.append(rec)

    for i in users[user]:
        for rec in recommend(i):
            recomended_films.append(rec)

    films = []
    for rec in recomended_films:
        films.append(filmoteka[rec])

    user_films = []
    ufs=users[user]
    for uf in ufs:
        user_films.append(filmoteka[uf])

    return render_template('index.html', films=films, user_films=user_films, genres=genres, user=user, users=users)


def format_vector(text, genre):
    if text == None:
        text = []
    tk = Tokenizer()
    res = tk.encode(text, "tokenizer/tokens_encode.json")
    if(len(res)<964):
        res.extend([0] * (964 - len(res)))
    else:
        res = res[0:964]
    res = [num / 11990 for num in res]
    vector = predict(res)[0].tolist()
    vector.append(float(genre))
    vector.append(90/455)
    return vector


if __name__ == '__main__':
    # print()
    app.run(debug=True, host="0.0.0.0", port=8080)

