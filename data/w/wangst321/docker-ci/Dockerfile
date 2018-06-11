# start with a base image  
FROM ubuntu:14.10  
# install dependencies  
RUN apt-get -y update  
RUN apt-get install -y python python-dev python-pip python-psycopg2  
RUN apt-get install -y nginx supervisor  
  
# add requirements.txt and install  
# ADD requirements.txt /code/requirements.txt  
ADD . /code  
# set working diretory  
WORKDIR /code  
  
RUN pip install -r requirements.txt  
  

