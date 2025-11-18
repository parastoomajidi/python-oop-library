"""Manages a collection of Book objects."""
class Library:
    
    """Initializes a new, empty library."""
    def __init__(self):
        self.books = {}

    # ---------------------------------------
    def add_book(self, book):
        
        """
                Adds a Book object to the library.
                
                Prevents duplicates based on ISBN.
                
                Args:
                    book (Book): The Book object to add.
                """
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
