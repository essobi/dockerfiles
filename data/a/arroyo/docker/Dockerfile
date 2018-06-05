############################################################  
# Docker Compose Container  
#  
# Simple container for continuous integration that includes  
# Docker and Docker Compose  
############################################################  
  
FROM ubuntu:16.10  
  
# File Author / Maintainer  
MAINTAINER John Arroyo, john@arroyolabs.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl git wget  
  
RUN VER="17.03.1-ce" && \  
curl -L -o /tmp/docker-$VER.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$VER.tgz && \  
tar -xz -C /tmp -f /tmp/docker-$VER.tgz && \  
mv /tmp/docker/* /usr/bin  
  
RUN curl -L https://github.com/docker/compose/releases/download/1.11.2/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  
  
RUN mkdir /code && apt-get clean  
  
ENTRYPOINT ["tail", "-f", "/dev/null"]  

