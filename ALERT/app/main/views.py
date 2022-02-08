from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_all_news_sources,get_business_headlines
# get_all_news_headlines
#views

@main.route('/')
def index():
    '''
    view root page returns index page and its data
    '''
    #getting headlines
    all_news_sources = get_all_news_sources('sources')
    business_headlines = get_business_headlines()
    # all_news_headlines = get_all_news_headlines()

    #now_showing_news =get_news('now_showing')

    title='NEWS ALERT!'

   
    return render_template('index.html',sources= all_news_sources,title=title,business=business_headlines)
  