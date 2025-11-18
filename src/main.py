from book import Book
from library import Library


book1 = Book("1984", "George Orwell", "026")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "027")
book3 = Book("To Kill a Mockingbird", "Harper Lee", "027")  # duplicate ISBN

my_library = Library()

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

my_library.find_book_by_isbn("999")
my_library.list_books()
