FROM python:3.4  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update -qq && apt-get install -y postgresql-client libpq-dev git-
core libmemcached-dev ruby-sass ruby-compass libxml2-dev libxslt1-dev libjpeg-
dev  
RUN mkdir /code  
WORKDIR /code  
ADD requirements.txt /code/  
RUN pip install -r requirements.txt  
ADD . /code/  

