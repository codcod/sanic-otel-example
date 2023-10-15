import os

from prometheus_client import multiprocess
from sanic import Sanic

from .app_factory import create_app
from .log import app_logger

app = create_app()


@app.main_process_start
def display_routes(app_: Sanic, _):
    app_logger.info('Registered routes:')
    for route in app_.router.routes:
        app_logger.info('> /%s', route.path)


@app.after_server_stop
def after_server_stop(_app, _loop):
    multiprocess.mark_process_dead(os.getpid())
