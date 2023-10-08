import os

from opentelemetry.exporter.prometheus import PrometheusMetricReader
from opentelemetry.metrics import set_meter_provider
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.resources import Resource
from prometheus_client import multiprocess as prom_multi
from sanic.log import logger

from .app_factory import create_app

app = create_app()


@app.main_process_start
def display_routes(sanic_app, _):
    logger.info('Registered routes:')
    for route in sanic_app.router.routes:
        logger.info('> /%s', route.path)


def configure_meter_provider():
    reader = PrometheusMetricReader(prefix='bookstore')
    provider = MeterProvider(metric_readers=[reader], resource=Resource.create())
    set_meter_provider(provider)


@app.after_server_start
async def after_server_start(_app, _loop):
    configure_meter_provider()
    # prom.start_http_server(addr='127.0.0.1', port=9000)


@app.after_server_stop
def after_server_stop(_app, _loop):
    prom_multi.mark_process_dead(os.getpid())
