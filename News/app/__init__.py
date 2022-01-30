from flask import Flask 
from .config import DevConfig
#intialize application 
app = Flask(__name__)
from app import views