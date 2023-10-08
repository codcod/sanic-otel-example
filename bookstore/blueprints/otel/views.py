import prometheus_client as prom
from prometheus_client import multiprocess as prom_multi
from sanic import Blueprint
from sanic import Request
from sanic import Sanic
from sanic.response import raw

bp = Blueprint('OTel', url_prefix='/')


@bp.route('/metrics')
async def metrics(_req: Request):
    app = Sanic.get_app()
    if app.config.MULTIPROC:
        registry = prom.CollectorRegistry()
        prom_multi.MultiProcessCollector(registry)
    else:
        registry = prom.core.REGISTRY
    data = prom.exposition.generate_latest(registry)
    print(f'{data=}')
    return raw(data, content_type=prom.CONTENT_TYPE_LATEST)
