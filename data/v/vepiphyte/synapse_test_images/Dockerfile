FROM python:3.6  
MAINTAINER vEpiphyte <epiphyte@vertex.link>  
  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update  
  
RUN mkdir -p /opt/reqs/build/  
  
COPY requirements.txt /opt/reqs/build/requirements.txt  
  
RUN pip install -r /opt/reqs/build/requirements.txt

