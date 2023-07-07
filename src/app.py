import os, jwt
from flask import Flask, render_template, request, flash, redirect, url_for
from auth_middleware import token_required
from main import session
from models import User, Article
from sqlalchemy import select

app = Flask(__name__)

SECRET_KEY = os.environ.get('SECRET_KEY') or 'this is a secret'
print(SECRET_KEY)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
# def index():
#     articles = session.query(Article).all()
#     return render_template('index.html', articles=articles)

@app.route("/sign-in")
def addUser():
    pass

