FROM python:2-alpine  
MAINTAINER Oscar Prieto <oscarmpp@gmail.com>  
  
# Install packages  
RUN apk add --no-cache ca-certificates libstdc++  
  
# Install packages only needed for building  
RUN apk add --no-cache --virtual .build-dependencies build-base \  
&& pip install locustio pyzmq influxdb \  
&& apk del .build-dependencies  
  
# Create a workdir  
RUN mkdir /locust  
WORKDIR /locust  
EXPOSE 8089  

