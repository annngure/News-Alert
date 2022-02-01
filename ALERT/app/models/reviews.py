class Review:
    all_reviews=[]

    def __init__(self,image,title,description,url,time,content):
        self.image =image
        self.title =title
        self.description=description
        self.url=url
        self.time=time
        self.content=content
    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()
        