# Retrieve.md

## Python Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
```
## Comment
Expected Output:
('1984', 'George Orwell', 1949)

The book record was successfully retrieved with all its attributes.
