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