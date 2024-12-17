from flask import Flask, render_template
import json

app = Flask(__name__)

with open("data/for_web.json", 'r', encoding='utf-8') as file:
    filmoteka = json.load(file)

@app.route('/')
def index():
    recomended_films = ["1343","1216", "1155"]
    films = []
    for rec in recomended_films:
        films.append(filmoteka[rec])

    user_films = []
    ufs=["18"]
    for uf in ufs:
        user_films.append(filmoteka[uf])

    return render_template('index.html', films=films, user_films=user_films)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

