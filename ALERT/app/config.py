import os

class Config:
    '''
    General configuration parent class
    '''
    SOURCE_API_BASE_URL='https://newsapi.org/v2/everything?q={}from=2022-02-01&sortBy=popularity&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    TOP_HEADLINES_BASE_API_URL='https://newsapi.org/v2/everything?q=top%20headlines&from=2022-02-01&sortBy=popularity&apiKey={}'
    BUSINESS_TOP_HEADLINES='https://newsapi.org/v2/everything?q=business&from=2022-02-01&sortBy=popularity&apiKey={}'
class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config : The parent configuration class with General configuration settings
    '''
class DevConfig(Config):
    '''
    Development configuration child class

    Args:
    Config: The parent configuration class with General configuration settings

    '''
    DEBUG = True
    
    config_options = {
        # 'development':DevConfig,
        'production': ProdConfig
    }