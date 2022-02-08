import os

class Config:
    '''
    General configuration parent class
    '''
    # breakpoint()
    SOURCE_BASE_API_URL='https://newsapi.org/v2/top-headlines/{}?apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    TOP_HEADLINES_BASE_API_URL='https://newsapi.org/v2/top-headlines?{}&apiKey={}'
    BUSINESS_TOP_HEADLINES_URL='https://newsapi.org/v2/top-headlines/sources?category=business&apiKey={}'
   
class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config : The parent configuration class with General configuration settings
    '''
    
class DevConfig(Config):
 
    DEBUG = True

    

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}