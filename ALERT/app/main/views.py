from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_all_news_sources,get_all_news_headlines,get_business_headlines,search_articles
#views
@main.route('/')
def index():
    '''
    view root page returns index page and its data
    '''
    #getting headlines
    all_news_sources = get_all_news_sources('source')
    business_headlines = get_business_headlines()

    #now_showing_news =get_news('now_showing')

    title='NEWS ALERT!'

    # search_news = request.args.get('news_query')
    return render_template('index.html',source= all_news_sources,title=title,business_headlines=business_headlines)
    # if search_news:
    #     return redirect(url_for('.search',source_name=search_news))
    # else:
    #     return render_template('index.html',source= all_news_sources,title=title,business_headlines=business_headlines)


@main.route('/source/<int:title>')
def news_headlines(title):
    '''
    View root page fuction that returns the index page and its data
    '''
    
    news = get_all_news_headlines(title)
    title = f'{news.title}'

    return render_template('news.html',title = title,headlines = news_headlines)

@main.route('/search/<source_name>')
def search(source_name):
    '''
    view function to dispaly the search results

    '''
    source_name_list = source_name.split("source")
    source_name_format = "+".join(source_name_list)
    searched_sources = search_articles(source_name_format)
    title =f'search result for {source_name}'
    return render_template('search.html',results = searched_sources)