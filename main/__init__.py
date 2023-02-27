from flask import Flask
from secrets import choice as secrets_choice
import string
import os

# Secret key length variables
secretkeylength = 44

keyfilecheck = os.path.exists('temp/secretkey.txt')

if keyfilecheck == False:
    os.mkdir('temp')
    secretkeygen = ''.join(secrets_choice(string.ascii_letters + string.digits) for i in range(secretkeylength))
    with open('temp/secretkey.txt', 'w') as f:
        f.write(secretkeygen)

keyfile = open('temp/secretkey.txt', 'r')
secretkey = keyfile.read()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secretkey
    app.config['UPLOAD_FOLDER'] = 'uploads/'
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    return app

keyfile.close()