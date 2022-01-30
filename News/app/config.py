import os

class Config:
    '''
    configuration parent class
    '''
class ProdConfig(Config):
    '''
    configuration child class

    '''
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    #To enable debug mode.
    DEGBUG = True

config_options ={
    'development':DevConfig,
    'production':ProdConfig
}
