.ONESHELL:
.PHONY: clean install run


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

docker_run:
	python manage.py run