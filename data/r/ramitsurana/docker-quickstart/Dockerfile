# Dockerfile for docker image of Docker-quickstart  
FROM ubuntu  
  
MAINTAINER Ramit Surana "ramitsurana@gmail.com"  
RUN apt-get update -y  
RUN apt-get install curl -y  
RUN curl -sSL https://get.docker.com/ | sh  
RUN curl -L https://github.com/docker/compose/releases/download/1.7.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
RUN docker run hello-world  
  
CMD ["/docker-quickstart"]  

