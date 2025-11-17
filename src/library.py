class Library:
    def __init__(self):
        self.books= []

    def add_book(self, book):
        # add book
        self.books.append(book)

    def list_book(self):
        if not self.books:
            print("the library is empty")
        for book in self.books:
            print(book)


