from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting the api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets json response to the url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data =url.read()
        get_news_response = json.loads(get_news_data)

        news_result = None
        
        if get_news_response['results']:
            news_result_list = get_news_response['result']
            news_result = process_results(news_result_list)
        return news_result

def process_results(news_list):
    '''
    Function that process the result and transform them into a list of objects
    
    Args:
       news_list :it contains news details

    returns:
        news_result : A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        headlines= news_item.get('headlines')
        image=news_item.get('image')
        shortstory=news_item.get('shortstory')

        if poster:
            news_object =News(headlines,image,shortstory)
            news_result.append(news_object)
        return news_result