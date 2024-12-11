from flask import Flask, render_template
import json

app = Flask(__name__)

with open("data/for_web.json", 'r', encoding='utf-8') as file:
    filmoteka = json.load(file)

@app.route('/')
def index():
    recomended_films = ["0", "1", "120", "1000", "3001", "3042", "210", "3", "4", "5", "12", "989"]

    films = []

    for rec in recomended_films:
        films.append(filmoteka[rec])

    return render_template('index.html', films=films)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

