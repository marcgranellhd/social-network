# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
from models import db, User
app = Flask(__name__)


@app.route("/")
def signup():
    return render_template('signup.html')


@app.route("/comprobarEmail/<email>")
def buscar(email):
    num_resultados = User.query.filter_by(email=email).count()
    return str(num_resultados)


if __name__ == "__main__":
    app.debug = True
    app.run()
