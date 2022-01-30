from os import environ env

class Config:
    '''
    configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/api_key={}'
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