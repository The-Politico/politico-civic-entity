test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

dev:
	gulp --cwd entity/staticapp/

database:
	dropdb entity --if-exists
	createdb entity
