################################  
# Dockerfile for EventRetrieve #  
# BigDataEurope #  
# #  
# git 1.9.1 #  
# Python 2.7 #  
# Django 1.10.5 #  
################################  
  
FROM ubuntu:14.04  
MAINTAINER Giorgos Argyriou <gioargyr@gmail.com>  
  
# INSTALL PREREQUISITIES  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
curl \  
git \  
python-pip \  
vim \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install django \  
&& mkdir /input \  
&& git clone -b poolparty https://github.com/big-data-europe/BigDataEurope-
EventDetectionService.git  
  
EXPOSE 8000  
  
WORKDIR /BigDataEurope-EventDetectionService  
  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

