from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from model import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')