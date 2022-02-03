from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

#Initializing application
app = Flask (__name__,instance_relative_config = True)

#Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')

app.config.from_object(config_options[config_name])

#Initializing Flask Extensions
bootstrap.init_app(app)

from app import views
from app import error

return app