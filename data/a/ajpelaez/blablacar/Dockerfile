FROM python:3  
MAINTAINER Antonio Jesus Pelaez Priego  
  
WORKDIR /  
COPY . .  
RUN pip install --no-cache-dir -r requirements.txt  
EXPOSE 80  
CMD gunicorn --chdir ./FindBlaBlaCarBot -b 0.0.0.0:80 api:__hug_wsgi__ --log-
level=debug --timeout=40  

