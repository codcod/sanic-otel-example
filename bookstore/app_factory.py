import os
import typing as tp

from sanic import Sanic

from .discovery import autodiscovery
from .log import setup_logging

Packages = tp.Sequence[str]

DEFAULT_BLUEPRINTS = [
    'bookstore.blueprints.books.views',
    'bookstore.blueprints.metrics.views',
]


def create_app(blueprints: Packages | None = None) -> Sanic:
    app = Sanic('Bookstore')
    app.config.MULTIPROC = 'PROMETHEUS_MULTIPROC_DIR' in os.environ
    setup_logging(app)

    if not blueprints:
        blueprints = DEFAULT_BLUEPRINTS

    autodiscovery(app, *blueprints)

    return app
