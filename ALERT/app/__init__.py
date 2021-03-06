from flask import Flask
from .config import DevConfig,config_options
from flask_bootstrap import Bootstrap
# from config import config_options
# import app


bootstrap = Bootstrap()

def create_app(config_name):

    #Initializing application
    app = Flask (__name__)

    #Setting up configuration
    app.config.from_object(config_options[config_name])

    # setting config
    from .request import configure_request
    configure_request(app)

    #Initializing Flask Extensions
    bootstrap.init_app(app)

    #Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app






  
