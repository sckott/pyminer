.PHONY: install test docs

install:
	uv pip install .

test:
	uv run pytest --record-mode=once --cov-report term --cov=pyminer test/

test_no_vcr:
	uv run pytest --disable-recording --cov-report term --cov=pyminer test/

docs:
	cd docs;\
	make html

opendocs:
	open docs/_build/html/index.html

clean:
	rm -rf dist/* build/*

dist:
	python -m build

lint-fix:
	uv run ruff check --select I --fix pyminer

lint-check:
	uv run ruff check pyminer

format-fix:
	uv run ruff format pyminer

format-check:
	uv run ruff format --check pyminer

ipython:
	uv run --with rich --with ipython python -m IPython

py:
	uv run python
