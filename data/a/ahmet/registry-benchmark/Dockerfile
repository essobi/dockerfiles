FROM golang:1.5-onbuild  
MAINTAINER Ahmet Alp Balkan  
  
ENV DOCKER_VERSION 1.8.1  
RUN wget -qO /usr/local/bin/docker
https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION} && \  
chmod +x /usr/local/bin/docker  
RUN docker -v  
  
ENTRYPOINT ["go-wrapper", "run"]  

