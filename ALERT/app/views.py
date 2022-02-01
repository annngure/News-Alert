from flask import render_template
from app import app
from .request import get_news,get_news
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