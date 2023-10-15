from prometheus_client import Counter

from bookstore.blueprints.books.model import Genre

LABEL_GENRE = 'genre'

books_added_counter = Counter(
    'bookstore_books_added_items_total', 'Books added to library', [LABEL_GENRE]
)

# Initiate counter with zeros for every choice of 'genre' label
for g in Genre.list():
    books_added_counter.labels(g)

books_borrowed_counter = Counter(
    'bookstore_books_borrowed_items_total', 'Books borrowed from library', [LABEL_GENRE]
)

# Initiate counter with zeros for every choice of 'genre' label
for g in Genre.list():
    books_borrowed_counter.labels(g)
