class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL='https://newsapi.org/2/news/{}?api_key={}'
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