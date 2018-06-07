FROM python:2.7-onbuild  
CMD ["gunicorn", "-c", "gunicorn_conf.py", "backend.wsgi:application", "--
reload"]

