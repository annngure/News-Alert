class Headlines:
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

class Everything:
    '''
    define the design of everything class
    '''
    def __init__(self,image,title,description,url,time,content):
        self.image=image #image of the news
        self.title=title
        self.description=description
        self.url=url
        self.time=time
        self.content=content

class Business:
     '''
    define the design of bisuness class
     '''
     def __init__(self,image,title,description,url,time,content):
        self.image=image #image of the news
        self.title=title
        self.description=description
        self.url=url
        self.time=time
        self.content=content

class Sources:
    '''
    this cover every data in the project
    '''
    def __init__(self,image,title,description,url,time,content):
        self.image=image #image of the news
        self.title=title
        self.description=description
        self.url=url
        self.time=time
        self.content=content