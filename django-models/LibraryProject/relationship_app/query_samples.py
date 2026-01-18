from relationship_app.models import Author, Book, Library, Librarian
# List all books in a library
Library.objects.get(name="library_name")
#library_books = library.books.all()

# Query all books by a specific author
author = Author.objects.get(name="author_name")
books_by_author = Book.objects.filter(author=author)


# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
