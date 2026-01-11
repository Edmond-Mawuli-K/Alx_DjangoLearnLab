---
# Update.md

## Python Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book.title
```

## Comment
Expected Output:
'Nineteen Eighty-Four'

The book title was successfully updated and saved to the database.
