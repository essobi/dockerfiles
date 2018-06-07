FROM kennethzfeng/dockerize-python:2.7.8-onbuild  
EXPOSE 8000  
CMD ["gunicorn", "app:app", "--worker-class", "gevent", "-b", "0.0.0.0:8000"]  

