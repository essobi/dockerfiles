FROM python:2.7-slim  
MAINTAINER Nick Janetakis <nick.janetakis@gmail.com>  
  
# 1 issue but harmless: debconf: delaying package configuration, since apt-
utils is not installed  
# https://github.com/phusion/baseimage-docker/issues/319  
RUN apt-get update && apt-get install -qq -y apt-utils build-essential libpq-
dev postgresql-client-9.4 --fix-missing --no-install-recommends  
  
ENV INSTALL_PATH /mobydock  
RUN mkdir -p $INSTALL_PATH  
  
WORKDIR $INSTALL_PATH  
  
COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
  
COPY . .  
  
VOLUME ["static"]  
  
CMD gunicorn -b 0.0.0.0:8000 "mobydock.app:create_app()"  
  

