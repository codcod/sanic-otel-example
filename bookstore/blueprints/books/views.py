import time
import uuid

from sanic import Blueprint
from sanic import HTTPResponse
from sanic import Request
from sanic import json

from bookstore.blueprints.otel.metrics import books_added_counter
from bookstore.blueprints.otel.metrics import books_borrowed_counter

from .model import random_book

bp = Blueprint('Book', url_prefix='/book')


@bp.get('/add')
async def add_book_handler(_req: Request) -> HTTPResponse:
    msg = {
        'uuid': uuid.uuid4().hex,
        'time': time.time(),
        'operation': 'add',
    }

    books_added_counter.add(1)

    return json(msg, status=202)


@bp.get('/borrow-random')
async def borrow_book_handler(_req: Request) -> HTTPResponse:
    msg = {
        'uuid': uuid.uuid4().hex,
        'time': time.time(),
        'operation': 'borrow',
    }

    books_borrowed_counter.add(1, random_book())

    return json(msg, status=202)
