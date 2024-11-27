import os
import django

# Configure the settings for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_id):
    # Query all books by a specific author
    try:
        author = Author.objects.get(id=author_id)
        books = Book.objects.filter(author=author)
        print(f"Books written by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author with ID {author_id} does not exist.")

def list_all_books_in_library(library_id):
    # List all books in a library
    try:
        library = Library.objects.get(id=library_id)
        books = library.books.all()  # Corrected to access the related books
        print(f"Books in the library {library.name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library with ID {library_id} does not exist.")

def retrieve_librarian_for_library(library_id):
    # Retrieve the librarian for a library
    try:
        library = Library.objects.get(id=library_id)
        librarian = library.librarian  # Corrected to access the related librarian
        print(f"The librarian for the library {library.name} is {librarian.name}.")
    except Library.DoesNotExist:
        print(f"Library with ID {library_id} does not exist.")

if __name__ == '__main__':
    # Example usage
    query_books_by_author(1)
    list_all_books_in_library(1)
    retrieve_librarian_for_library(1)
    



