from flask import render_template
from app import app
from .request import get_news,get_news,search_news
#views
@app.route('/news/<int:title>')
def news(title):
    '''
    View root page fuction that returns the index page and its data
    '''
    #getting headlines
   
    # business_news=get_news('popular')
    # print(business_news)
    # title='NEWS ALERT!'
    # return render_template('index.html',title=title,business=business_news)
    news = get_news(title)
    title = f'{news.title}'

    return render_template('news.html',title = title,news = news)

@app.route('/search/<news_name>')
def search(news_name):
    '''
    view function to dispaly the search results

    '''
    news_name_list = news_name.split('')
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title =f'search result for {news_name_format}'
    return render_template('search.html',news = searched_news)