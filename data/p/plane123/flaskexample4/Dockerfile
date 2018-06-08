# Dockerfile for a simple Flask application  
FROM python:3-onbuild  
EXPOSE 8000  
CMD [ "gunicorn","-c", "gunicorn_config.py", "flask-example:app" ]  

