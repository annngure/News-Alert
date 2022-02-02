from app import app
import urllib.request,json
from .models import news,headlines,business

News = news.News

#the  api keys available
api_key = app.config['NEWS_API_KEY']
sources_url= app.config['SOURCE_BASE_API_URL']
top_headlines_news_url=app.config['TOP_HEADLINES_BASE_API_URL']
business_top_headlines_url=app.config['BUSINESS_TOP_HEADLINES']
# base_url = app.config['NEWS_API_BASE_URL']

def get_all_news_sources(source):
    '''
    Function that gets json response to the url request
    '''
    get_news_url = sources_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
          sources_data =url.read()
          sources_response = json.loads(source_data)
          sources_result = None
          if sources_response['results']:
             sources_items = source_response['results']
             sources_results = process_results(source_items)
    return sources_results

def process_results(source_list):
    '''
    Function that process the result and transform them into a list of objects
    
    Args:
       news_list :it contains news details

    returns:
        news_result : A list of news objects
    '''
    sources_results = []
    for news_item in sources_list:
        image=news_item.get('image')
        title=news_item.get('title')
        description=news_item.get('description')
        url=news_item.get('url')
        time=news_item.get('publisheAt')
        content=news_item.get('content')
        new_source =News(image,title,description,url,publisheAt,content)
        sources_results.append(news_object)
    
    return sources_results



def get_all_news_headlines(source):
    '''
    function to pass top-headlines
    '''
    top_headlines_news_url= top_headlines_news_url.format(source,api_key)

    with urllib.request.urlopen(top_headlines_news_url) as url:
        headlines_data = url.read()
        headlines_response = json.loads(headlines_data)
        headlines_results = None
        if headlines_response['results']:
            headlines_itens = headlines_response['results']
            headlines_results = process_all_headlines_data(headlines_list)
    return headlines_results

def process_all_headlines_data(headlines_list):
    """
   Converting  data given as the Top-Headlines class.
    """
    headlines_processed_results = []
    for news_item in headlines_list:
        image=news_item.get('image')
        title=news_item.get('title')
        description=news_item.get('description')
        url=news_item.get('url')
        time=news_item.get('publisheAt')
        content=news_item.get('content')
        new_headlines =Headlines(image,title,description,url,publisheAt,content)
        headlines_processed_results.append(news_headlines)
    return  headlines_processed_results
#popular news
def get_popular_news():
    '''
    function will get popular news and then to pass response to process_all_porpular
    '''
    popular_news_url = popular_news_url.format(api_key)

    with urllib.request.urlopen(popular_news_url) as url:
        popular_data = url.read()
        popular_response = json.loads(popular_data)
        popular_results = None

        if popular_response['results']:
            popular_results_list = popular_response['results']
            popular_results = process_all_popular_results(popular_results_list)
    return popular_results


def process_all_popular_results(popular_results_list):
    '''
    responsible to convert data passed through get_popular_news() method
     '''
    popular_results = []
    for news_item in popular_results_list:
        image=news_item.get('image')
        title=news_item.get('title')
        description=news_item.get('description')
        url=news_item.get('url')
        time=news_item.get('publisheAt')
        content=news_item.get('content')
        new_popular =Popular(image,title,description,url,publisheAt,content)
        popular_results.append(news_popular)
    return  popular_results

#business news

def get_business_headlines():
    '''
    get business headlines and pass response to process_all_business_result()method
    '''
    business_headlines_url = business_top_headlines_url.format(api_key)
    with urllib.request.urlopen(business_headlines_url) as url:
        business_headlines_data = url.read()
        business_headlines_response = json.loads(business_headlines_data)
        business_headlines_results = None
        if business_headlines_response['results']:
           business_headlines_results_list = business_headlines_response['results']
           business_headlines_results = process_all_business_result(business_headlines_results_list)
    return business_headlines_results

def process_all_business_headlines_results(business_headlines_results_list):
    '''
    responsible to convert data passed through get_business_headlines() method
    '''
    
    business_headlines_results = []
    for news_item in business_headlines_results_list :
        image=news_item.get('image')
        title=news_item.get('title')
        description=news_item.get('description')
        url=news_item.get('url')
        time=news_item.get('publisheAt')
        content=news_item.get('content')

        business_headlines_object = Business(image,title,description,url,publisheAt,content)
        business_headlines_results.append(business_headlines_object)
        
    return business_headlines_results


# search news
def search_news(source):
    search_news_url='https://newsapi.org/v2/everything?q={}&apiKey={}'.formart(source,api_key)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            search_news_results = process_all_business_headlines_results(search_news_list)

    return search_news_results