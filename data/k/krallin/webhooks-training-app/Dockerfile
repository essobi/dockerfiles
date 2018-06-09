FROM python:3.4-onbuild  
EXPOSE 8000  
CMD ["gunicorn", "--access-logfile=-", "--error-logfile=-", "--
bind=0.0.0.0:8000", "wsgi:app"]  

