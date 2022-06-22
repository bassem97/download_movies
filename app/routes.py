import form as form
from flask import render_template

from app import app


@app.route('/')
def home():
    languages = ["C++", "Python", "PHP", "Java", "C", "Ruby",
                 "R", "C#", "Dart", "Fortran", "Pascal", "Javascript"]
    return render_template('home.html', languages=languages)


@app.route('/chooseMovie')
def chooseMovie():
    name = form.get('title')


app.run()
