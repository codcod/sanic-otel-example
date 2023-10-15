Sanic OpenTelemetry example
===========================

Sanic application that uses Prometheus Metrics API directly to export data to
Prometheus.

Next step would be to replace Prometheus calls with OpenTelemetry ones:
* opentelemetry-api
* opentelemetry-sdk
* opentelemetry-propagator-b3
* opentelemetry-exporter-prometheus

Libraries to install then:

    $ poetry add opentelemetry-{api,sdk,propagator-b3,exporter-prometheus}


Development
-----------

Run:

    $ make venv  # one time
    $ make run   

In a separate terminal:

    $ make prom-start
    $ open http://127.0.0.1:9090
    $ make k6
    $ make prom-stop

Linux users: replace in `docker/prometheus.yml`:

    - targets: ['host.docker.internal:1337']

with:

    - targets: ['127.0.0.1:1337']


Result:

![Prometheus](docs/prometheus.png)
