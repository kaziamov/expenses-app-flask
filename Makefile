full-test:
	poetry run pytest --show-capture=stdout --showlocals -vv
light-test:
	poetry run pytest --no-summary --disable-pytest-warnings
lint:
	poetry run flake8 expenses_app tests
check: light-test lint
push: check
	git push


install:
	poetry install
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl --force
test-coverage:
	poetry run pytest --cov=expenses_app --cov-report xml


# DEV

dev:
	poetry run flask --app expenses_app:app --debug run

server:
	sudo service postgresql start



py:
	poetry run python

run-db:
	docker-compose -f docker-compose.db.yml up --force-recreate

up:
	docker-compose   -f docker-compose.yml up --force-recreate

#  PROD

start:
	poetry run gunicorn --preload -w 5 -b 0.0.0.0:5000 expenses_app:app