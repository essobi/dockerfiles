FROM ubuntu:latest  
MAINTAINER Geert  
  
ENV LANG en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
RUN locale-gen $LANG  
RUN sed -i 's/restricted$/restricted multiverse/' /etc/apt/sources.list &&\  
apt-get update  
ADD https://github.com/jwilder/dockerize/releases/download/v0.0.2/dockerize-
linux-amd64-v0.0.2.tar.gz /dockerize-linux-amd64-v0.0.2.tar.gz  
RUN tar -C /usr/local/bin -xzvf /dockerize-linux-amd64-v0.0.2.tar.gz &&\  
rm /dockerize-linux-amd64-v0.0.2.tar.gz  
  
CMD /bin/sh

