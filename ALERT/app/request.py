import os
import urllib.request,json
from  .models import Sources,Business,Headlines
import app

# Keys
api_key = None
sources_url = None
top_headlines_news_url = None
business_top_headlines_url = None
everything_news_url = None


def configure_request(app):
    global api_key,sources_url,top_headlines_news_url,business_top_headlines_url,everything_news_url
    #the  api keys available
    api_key = app.config['NEWS_API_KEY']
    sources_url= app.config['SOURCE_BASE_API_URL']
    top_headlines_news_url=app.config['TOP_HEADLINES_BASE_API_URL']
    business_top_headlines_url=app.config['BUSINESS_TOP_HEADLINES_URL']

def get_all_news_sources(source):
    '''
    Function that gets json response to the url request
    '''
 
    get_news_url = sources_url.format(source,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        sources_data =url.read()
        sources_response = json.loads(sources_data)
        sources_articles = None
        if sources_response['sources']:
            sources_items = sources_response['sources']
            sources_articles = process_articles(sources_items)
    return sources_articles


def process_articles(sources_list):
    '''
    Function that process the result and transform them into a list of objects
    
    Args:
       news_list :it contains news details

    returns:
        news_result : A list of news objects
    '''
    sources_articles = []
    for news_item in sources_list:
        id=news_item.get('id')
        name=news_item.get('name')
        author=news_item.get('author')
        title=news_item.get('title')
        image=news_item.get('urlToImage')
        description=news_item.get('description')
        url=news_item.get('url')
        time=news_item.get('publisheAt')
        content=news_item.get('content')
        new_source =Sources(id,name,author,title,image,description,url,time,content)
        sources_articles.append(new_source)
    
    return sources_articles

#business news

def get_business_headlines():
    '''
    get business headlines and pass response to process_all_business_result()method
    '''
    business_headlines_url = business_top_headlines_url.format(api_key)
    with urllib.request.urlopen(business_headlines_url) as url:
        business_data = url.read()
        business_response = json.loads(business_data)
        business_headlines_articles = None
        if business_response['sources']:
           business_headlines_items = business_response['sources']
           business_headlines_articles = process_business_articles(business_headlines_items)
    return business_headlines_articles

def process_business_articles(business_list):
    '''
    responsible to convert data passed through get_business_headlines() method
    '''
    
    business_headlines_articles = []
    for news_item in business_list :
        id=news_item.get('id')
        name=news_item.get('name')
        author=news_item.get('author')
        title=news_item.get('title')
        image=news_item.get('urlToImage')
        description=news_item.get('description')
        url=news_item.get('url')
        time=news_item.get('publisheAt')
        content=news_item.get('content')
        new_business = Business(id,name,author,title,image,description,url,time,content)
        business_headlines_articles.append(new_business)
        
    return business_headlines_articles

