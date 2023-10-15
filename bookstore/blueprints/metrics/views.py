from prometheus_client import CONTENT_TYPE_LATEST
from prometheus_client import CollectorRegistry
from prometheus_client.core import REGISTRY
from prometheus_client.exposition import generate_latest
from prometheus_client.multiprocess import MultiProcessCollector
from sanic import Blueprint
from sanic import Request
from sanic import Sanic
from sanic.response import raw

bp = Blueprint('Metrics', url_prefix='/')


@bp.route('/metrics')
async def metrics(_req: Request):
    app = Sanic.get_app()
    if app.config.MULTIPROC:
        registry = CollectorRegistry()
        MultiProcessCollector(registry)
    else:
        registry = REGISTRY
    data = generate_latest(registry)
    return raw(data, content_type=CONTENT_TYPE_LATEST)
