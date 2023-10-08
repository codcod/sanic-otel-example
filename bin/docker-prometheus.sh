#!/usr/bin/env bash

docker run -d --rm \
    --name prom-otel \
    -v $(pwd)/docker/prometheus.yml:/etc/prometheus/prometheus.yml \
    --network=host \
    prom/prometheus

# vim: ft=sh:sw=4:et:ai