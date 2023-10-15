import time
import uuid

from sanic import Blueprint
from sanic import HTTPResponse
from sanic import Request
from sanic import json

from bookstore.blueprints.metrics.prom import books_added_counter
from bookstore.blueprints.metrics.prom import books_borrowed_counter

from .model import Book

bp = Blueprint('Book', url_prefix='/book')


@bp.get('/add')
async def add_book_handler(_req: Request) -> HTTPResponse:
    book = Book()
    books_added_counter.labels(book.genre).inc()

    msg = {
        'uuid': uuid.uuid4().hex,
        'time': time.time(),
        'operation': 'add',
    }

    return json(msg, status=200)


@bp.get('/borrow')
async def borrow_book_handler(_req: Request) -> HTTPResponse:
    book = Book()
    books_borrowed_counter.labels(book.genre).inc()

    msg = {
        'uuid': uuid.uuid4().hex,
        'time': time.time(),
        'operation': 'borrow',
    }

    return json(msg, status=200)
