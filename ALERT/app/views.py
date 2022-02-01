from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,get_news,search_news
#views
@app.route('/')
def index():
    '''
    view root page returns index page and its data
    '''
#getting headlines
   
    popular_news=get_news('popular')
    # print(popular_news)
    upcoming_news=get_news('upcoming')
    now_showing_news =get_news('now_showing')

    title='NEWS ALERT!'

    search_news = request.args.get('news_query')
    
    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:

    return render_template('index.html',title=title,popular=popular_news,upcoming=upcoming_news,now_showing=now_showing_news)


@app.route('/news/<int:title>')
def news(title):
    '''
    View root page fuction that returns the index page and its data
    '''
    
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