import os
from typing import Optional
from typing import Sequence

from sanic import Sanic

from .discovery import autodiscovery

DEFAULT_BLUEPRINTS = [
    'bookstore.blueprints.books.views',
    'bookstore.blueprints.otel.views',
]


def create_app(
    init_blueprints: Optional[Sequence[str]] = None,
) -> Sanic:
    app = Sanic('Bookstore')

    app.update_config(
        {
            'MULTIPROC': os.environ.get('MULTIPROC', False)
            in ('yes', 'y', '1', 'true'),
        }
    )

    if not init_blueprints:
        init_blueprints = DEFAULT_BLUEPRINTS

    autodiscovery(app, *init_blueprints)

    return app
