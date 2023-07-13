all: install check test

install:
	@asdf install
	@pip install -U pip poetry
	@poetry install

test:
	@poetry run pytest $(path)

check:
	@poetry run pre-commit run $(task) --all-files

run:
	poetry run uvicorn app.main:app --host=0.0.0.0 --reload --log-config=logger-config.yml --env-file=.env
