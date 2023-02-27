from flask import Blueprint, render_template, request, redirect, url_for
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('about/')
def aboutpage():
    return render_template("about.html")

@views.route('upload/', methods=['GET','POST'])
def uploadpage():
    if request.method == 'POST':
        pass
