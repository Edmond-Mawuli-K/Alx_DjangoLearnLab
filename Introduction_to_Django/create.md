# Create.md

## Python Command
```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

## Comment
Expected Output:
<Book: Book object (1)>

The Book instance was successfully created and saved to the database.
