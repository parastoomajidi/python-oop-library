class Library:
    def __init__(self):
        self.books = {}

    # ---------------------------------------
    def add_book(self, book):
        """Add a book to the library if ISBN is unique."""
        if book.isbn in self.books.keys():
            print(f"Error: Book with ISBN {book.isbn} already exists.")
        else:
            self.books[book.isbn] = book
            print(f"Book '{book.title}' added successfully!")

    # ---------------------------------------
    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books.values():
                print(book)

    # --------------------------------
