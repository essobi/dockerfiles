FROM python:2.7  
COPY . /project  
  
RUN virtualenv /venv/www  
  
RUN /venv/www/bin/pip install -r /project/requirements.txt  
  
EXPOSE 9999  
WORKDIR /project  
  
CMD ["/venv/www/bin/gunicorn", "-b 0.0.0.0:9999", "-k gevent", "app:app"]  

