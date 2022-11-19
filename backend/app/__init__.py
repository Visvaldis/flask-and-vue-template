from flask import Flask
from flask_cors import CORS

import os
import tensorflow as tf

app=Flask(__name__,static_folder='static')
app.config['SECRET_KEY']='verySecretKey'

APP_ROOT=os.path.dirname(os.path.abspath(__file__))
CORS(app, resources={r'/*': {'origins': '*'}})

from app import routes
