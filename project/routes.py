from flask import render_template
from flask import request, jsonify
from flask import redirect
from flask import url_for
from flask import session

import bcrypt
import datetime
from decimal import Decimal
import json
from datetime import date
import re

from project import app


#Date time global variables for queries
today=datetime.date.today()
today_string=today.strftime("%Y-%m-%d")

@app.route("/")
def home():
    return render_template("home.html", title="homepage")

@app.route("/register")
def register():
    return render_template("login.html", title="Login")

@app.route("/login")
def login():
    return render_template("login.html", title="Login")

@app.route("/test")
def test():
    return render_template("test.html", title="Test")

# Define a route to handle the form submission and display the file content
@app.route('/read_file', methods=['POST'])
def read_file():
    try:
        # Get the file name and location from the form
        file_path = request.form['file_path']
        
        # Open and read the specified file
        with open(file_path, 'r') as file:
            file_content = file.read()
        return render_template('test.html', content=file_content)
    except FileNotFoundError:
        return "File not found."