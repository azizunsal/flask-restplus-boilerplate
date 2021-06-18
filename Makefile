.ONESHELL:
.PHONY: clean install run

IMAGENAME=flask-restplus-boilerplate
REPO=aunsal
VERSION=0.0.1
IMAGEFULLNAME=${REPO}/${IMAGENAME}:${VERSION}
DOCKER_BUILD_CONTEXT=.
DOCKER_FILE_PATH=Dockerfile

clean:
	rm -rf venv

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt

run:
	. venv/bin/activate; \
	python manage.py run

db_init:
	. venv/bin/activate; \
	python manage.py db init

db_migrate:
	. venv/bin/activate; \
	python manage.py db migrate

db_upgrade:
	. venv/bin/activate; \
	python manage.py db upgrade

db_info:
	. venv/bin/activate; \
	python ./manage.py db current

_run:
	python manage.py run

build:
	docker build -t ${IMAGEFULLNAME} $(DOCKER_BUILD_CONTEXT) -f $(DOCKER_FILE_PATH)