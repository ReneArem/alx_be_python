 # library_system.py

class Book:
    """Base class for all types of books."""

    def __init__(self, title, author):
        """Initialize the Book with a title and author."""
        self.title = title
        self.author = author

class EBook(Book):
    """Derived class representing an electronic book."""

    def __init__(self, title, author, file_size):
        """Initialize the EBook with a title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

class PrintBook(Book):
    """Derived class representing a print book."""

    def __init__(self, title, author, page_count):
        """Initialize the PrintBook with a title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """Class to manage a collection of books."""

    def __init__(self):
        """Initialize the Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of each book in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")

# main.py (provided for testing)
from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()
