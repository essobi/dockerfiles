FROM ubuntu:14.04  
MAINTAINER tech@texastribune.org  
  
RUN apt-get update && apt-get upgrade -y && apt-get update  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN apt-get -y install software-properties-common apt-transport-https  
  
RUN apt-get -y install python python-pip libpq-dev python-dev  
  
RUN pip install --upgrade pip  
RUN pip install --upgrade wheel setuptools virtualenv  

