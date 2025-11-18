class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    # ---------------------------------------
    def __str__(self):
        """Return a readable string for when a Book object is printed."""
        return (
            f"Title: {self.title}, Author: {self.author}, "
            f"ISBN: {self.isbn}"
        )
