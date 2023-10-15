.PHONY = venv fix run prom-start prom-stop k6

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S),Linux)
	COMPOSE_CMD:=docker compose
endif
ifeq ($(UNAME_S),Darwin)
	COMPOSE_CMD:=docker-compose
endif

export PYTHONPATH=.

venv:
	rm -rf .venv
	poetry install

fix:
	poetry run isort bookstore
	poetry run black bookstore
	poetry run flake8 bookstore
	poetry run pylint bookstore/**
	poetry run mypy bookstore
	poetry run ruff bookstore

run:
	rm -rf .instance
	mkdir .instance

	PROMETHEUS_MULTIPROC_DIR=$(CURDIR)/.instance \
	LOGGING_LEVEL=DEBUG \
	ENVIRONMENT=local \
	    ./bin/run \
		--workers=2

prom-start:
	./bin/docker-prometheus.sh

prom-stop:
	docker stop prom-otel

k6:
	k6 run ./tests/k6-books-borrow-random.js
