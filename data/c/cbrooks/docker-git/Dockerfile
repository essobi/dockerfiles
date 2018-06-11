# Docker and Git  
FROM docker:dind  
  
MAINTAINER Corey Brooks <c.brooks@alumni.ubc.ca>  
  
RUN apk update  
RUN apk add git wget py-pip  
RUN pip install docker-compose  
  
# Dockerize is a useful tool for our Docker Compose setup  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.1.0/dockerize-linux-
amd64-v0.1.0.tar.gz  
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.1.0.tar.gz  
  

