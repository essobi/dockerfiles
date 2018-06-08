############################################################  
# Dockerfile to build Python WSGI Application Containers  
# Based on Ubuntu  
############################################################  
  
FROM python:2.7-wheezy  
MAINTAINER Nick Clark  
  
RUN apt-get update  
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential  
RUN apt-get install -y python python-dev python-distribute python-pip  
  
ADD . /app  
  
# Get pip to download and install requirements:  
RUN pip install --upgrade pip && \  
pip install -r /app/requirements.txt  
  
# Expose ports  
EXPOSE 80  
  
# Set the default directory where CMD will execute  
WORKDIR /app  
  
# Set the default command to execute  
# when creating a new container  
# i.e. using CherryPy to serve the application  
CMD python run.py  

