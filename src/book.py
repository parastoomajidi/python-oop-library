class Book :
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

# show wich book showed when a book printed
    def __str__(self):
        return f"title:{self.title}, by author:{self.author}, (ISBN: {self.isbn})"