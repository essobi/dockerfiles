FROM python:alpine  
MAINTAINER Oscar Prieto <oscarmpp@gmail.com>  
  
# Install packages  
RUN apk add --no-cache ca-certificates libstdc++  
  
# Install packages only needed for building  
RUN apk add --no-cache --virtual .build-dependencies build-base  
  
# Pip stuff  
RUN pip install locustio==0.8a2 pyzmq influxdb  
  
# Remove unneed packages  
RUN apk del .build-dependencies  
  
# Create a workdir  
RUN mkdir /locust  
WORKDIR /locust  
EXPOSE 8089  

