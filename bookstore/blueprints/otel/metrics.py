from opentelemetry.metrics import get_meter_provider

meter = get_meter_provider().get_meter(
    name='bookstore_meter',
    version='0.1.2',
    schema_url='https://opentelemetry.io/schemas/1.9.0',
)
books_added_counter = meter.create_counter(
    'books_added', unit='items', description='Total number of books added to library'
)
books_borrowed_counter = meter.create_counter(
    'books_borrowed',
    unit='items',
    description='Total number of books borrowed from library',
)
