# app/__init__.py

from flask import Flask,render_template,url_for

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return render_template('home.html')

    @app.route('/game')
    def gamepage():
        return render_template('game.html')

    return app