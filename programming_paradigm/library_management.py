class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available (not checked out)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available, False if checked out."""
        return not self._is_checked_out


class Library:
    """Represents a library that can manage a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a new Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it’s available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Sorry, '{title}' is not available for checkout.")

    def return_book(self, title):
        """Return a checked-out book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"No book found with the title '{title}'.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
