# start with the base image  
FROM ubuntu:14.10  
# install dependencies  
RUN sudo sed -i -e 's/archive.ubuntu.com\|security.ubuntu.com/old-
releases.ubuntu.com/g' /etc/apt/sources.list  
  
RUN apt-get -y update  
RUN apt-get install -y python python-dev python-pip python-psycopg2  
RUN apt-get install -y nginx supervisor  
  
# add requirements.txt and install  
ADD requirements.txt /code/requirements.txt  
RUN pip install -r /code/requirements.txt  
  
# set working directory  
WORKDIR /code  
  
EXPOSE 80

