FROM python:3.6-slim  
  
WORKDIR /srv  
COPY . /srv  
  
RUN mkdir -p /srv/static  
  
RUN pip3 install -r /srv/requirements.txt  
  
RUN python3 manage.py collectstatic --no-input  
RUN python3 manage.py migrate --no-input  
  
EXPOSE 80  
CMD gunicorn --bind 0.0.0.0:80 titansgaming.wsgi  

