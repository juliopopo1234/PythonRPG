from flask import Flask, render_template, redirect, url_for
#Base
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/BddRPG"
mongo = PyMongo(app)

@app.route("/")
def index():
    return render_template("Home.html")

@app.route("/home")
def home():
    return render_template("Home.html")

@app.route("/game")
def game():
    return render_template("Game.html")

@app.route("/assets")
def assets():
    return 'Hello World'