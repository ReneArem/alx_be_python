# book_class.py

class Book:
    """Class representing a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message upon deletion of the Book instance."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official representation that recreates the Book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

# main.py (provided for testing)
from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the str method
    print(my_book)  # Expected to use str

    # Demonstrating the repr method
    print(repr(my_book))  # Expected to use repr

    # Deleting a book instance to trigger del
    del my_book

if __name__ == "__main__":
    main()
