class News:
    '''
    news class to define news object in testcase
    '''
    def __init__(self,image,title,description,url,time,content):
        self.image=image #image of the news
        self.title=title
        self.description=description
        self.url=url
        self.time=time
        self.content=content