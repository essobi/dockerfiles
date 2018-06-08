# start with a base image  
FROM ubuntu:14.04  
# install dependencies  
#RUN echo "deb http://cn.archive.ubuntu.com/ubuntu/ trusty main restricted" >
/etc/apt/sources.list  
#RUN echo "deb-src http://cn.archive.ubuntu.com/ubuntu/ trusty main
restricted" > /etc/apt/sources.list  
RUN apt-get -y update  
RUN apt-get install -y python python-dev python-pip python-psycopg2  
RUN apt-get install -y nginx supervisor  
  
# add requirements.txt and install  
ADD requirements.txt /code/requirements.txt  
RUN pip install -r /code/requirements.txt  
  
# set working diretory  
WORKDIR /code  

