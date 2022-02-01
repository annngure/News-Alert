from app import app
import urllib.request,json
from .models import news


breakpoint()
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
            news_result_list = get_news_response['results']
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
        image= news_item.get('image')
        title=news_item.get('title')
        description=news_item.get('description')
        url=news_item.get('url')
        time=news_item.get('publisheAt')
        content=news_item.get('content')
        if poster:
            news_object =News(image,title,description,url,publisheAt,content)
            news_result.append(news_object)
        return news_result
# getting to news
def get_news(title):
    get_news_details_url= base_url.format(title,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            image = news_details_response.get('urlToImage')
            title = news_details_response.get('title')
            description=news_details_response.get('description')
            url=news_details_response.get('url')
            time=news_details_response.get('publisheAt')
            content=news_details_response.get('content')
            news_object = News(image,title,description,url,publisheAt,content)
    return news_object

# search news
def search_news(news_name):
    search_news_url='https://newsapi.org/v2/everything?q={}&from=2022-02-01&sortBy=popularity&apiKey={}'.formart(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news-results = process_results(search_news_list)

        return search_news_results