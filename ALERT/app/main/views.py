from flask import render_template,request,redirect,url_for
from app import app
from .request import get_all_news_sources,get_all_news_headlines,get_business_headlines,search_news
#views
@app.route('/')
def index():
    '''
    view root page returns index page and its data
    '''
#getting headlines
   
    all_news_sources = get_all_news_sources()
    business_headlines = get_business_headlines()

  #  now_showing_news =get_news('now_showing')

    title='NEWS ALERT!'

    search_news = request.args.get('news_query')
    
    if search_news:
        return redirect(url_for('.search',source_name=search_news))
    else:

        return render_template('index.html',sources= all_news_sources,title=title,popular=popular_news,upcoming=upcoming_news,business_headlines=business_headlines)


@app.route('/source/<int:title>')
def news_headlines(title):
    '''
    View root page fuction that returns the index page and its data
    '''
    
    news = get_all_news_headlines(title)
    title = f'{news.title}'

    return render_template('news.html',title = title,headlines = news_headlines)

@app.route('/search/<source_name>')
def search(source_name):
    '''
    view function to dispaly the search results

    '''
    news_name_list = news_name.split('')
    news_name_format = "+".join(news_name_list)
    searched_sources = search_news(news_name_format)
    title =f'search result for {news_name}'
    return render_template('search.html',results = searched_sources)