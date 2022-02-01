from flask import render_template
from app import app
#views
@app.route('/')
def index():
    '''
    View root page fuction that returns the index page and its data
    '''
    #getting headlines
   
    business_news=get_news('popular')
    print(business_news)
    title='NEWS ALERT!'
    return render_template('index.html',title=title,business=business_news)