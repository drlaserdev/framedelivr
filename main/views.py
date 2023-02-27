from flask import Blueprint, render_template, request, redirect, url_for
from .forms import MediaForm
from werkzeug.utils import secure_filename
import os

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return redirect(url_for('views.upload'))

@views.route('about/')
def aboutpage():
    return render_template("about.html")

@views.route('upload/', methods=['GET','POST'])
def upload():
    form = MediaForm()
    if form.validate_on_submit() == True:
        f = form.file.data
        filename = secure_filename(f.filename)
        f.save(os.path.join('uploads/', filename))
        return redirect(url_for('views.aboutpage'))
    return render_template('upload.html', form=form)