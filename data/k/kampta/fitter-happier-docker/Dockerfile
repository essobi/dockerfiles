# start with a base image  
FROM ubuntu:14.04  
# install dependencies  
RUN apt-get update && apt-get install -y python python-dev python-pip python-
psycopg2 nginx supervisor  
  
# set working diretory  
WORKDIR /code  
COPY . /code  
  
# add requirements.txt and install  
RUN pip install -r /code/requirements.txt  
  

