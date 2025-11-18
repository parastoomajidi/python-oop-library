class Library:
    def __init__(self):
        self.books= {}
# ///////////////////////////////////////////
    def add_book(self, book):
        # add book
        if  book.isbn in self.books.keys():
            print(f"Error: Book with ISBN {book.isbn} already exists.")
        else:
            self.books[book.isbn] =  book
# ///////////////////////////////////////////

    def list_book(self):
        if not self.books:
            print("the library is empty")
        for book in self.books.values():
            print(book)
# ///////////////////////////////////////////

    def find_book_by_isbn(self, isbn):
        if self.books.get(isbn):
            print(self.books.get(isbn))
        else:
            print("not found")

