from app import app
import urllib.request,json
from .models from NEWS
#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    