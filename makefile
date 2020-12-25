prod:
	pipenv run python manage.py runserver --settings=cs302AlgorithmsProject.settings.production

dev:
	pipenv run python manage.py runserver

static:
	pipenv run python manage.py collectstatic

noinput:
	pipenv run python manage.py collectstatic --noinput