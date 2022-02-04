from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

#Initializing application
    app = Flask (__name__)

#Setting up configuration
    app.config.from_object(config_options[config_name])

#Registering blueprint
from .models import models as models_blueprint
app.register_blueprint(models_blueprint)

# setting config
from .requests import configure_request
configure_request(app)

#Initializing Flask Extensions
bootstrap.init_app(app)

# return app



  
