from flask import render_template, request
from . import main

@main.route('/ui')
def index():
    return render_template("index.html")

