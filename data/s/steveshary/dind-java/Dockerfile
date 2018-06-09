FROM docker:17.05-git  
MAINTAINER Stephen Shary <stephen.shary@gmail.com>  
  
# Define commonly used variables  
ENV LANG C.UTF-8  
ENV DOCKER_VERSION 17.05  
ENV COMPOSE_VERSION 1.14.0  
ENV JAVA_VERSION 7u121  
ENV JAVA_HOME /usr/lib/jvm/java-1.7-openjdk  
  
# Install Java.  
RUN \  
apk add --no-cache --update \  
curl \  
py-pip \  
openjdk7=7.121.2.6.8-r0 && \  
pip install docker-compose==1.14.0 && \  
rm -rf ~/.cache && \  
apk del py-pip && \  
rm -rf /var/cache/apk/*

