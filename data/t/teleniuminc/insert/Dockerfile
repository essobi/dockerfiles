FROM ubuntu:14.04.5  
MAINTAINER Telenium "github@telenium.ca"  
# Install python development packages, and pip  
RUN apt-get update -qy  
RUN apt-get install -y python-dev python-pip  
  
# Latest version of pip  
RUN pip install --upgrade pip  
  
# Install tox  
RUN pip install tox  

