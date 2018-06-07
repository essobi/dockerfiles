FROM ubuntu:14.04  
MAINTAINER Hussein Galal  
  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y python python-pip python-setuptools python-dev libpq-
dev libffi-dev  
  
ADD requirements.txt /app/requirements.txt  
RUN pip install -r /app/requirements.txt  
  
WORKDIR /app  

