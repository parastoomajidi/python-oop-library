class Book :
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __srt__(self):
        print (f"title:{self.title}, by author:{self.author}")