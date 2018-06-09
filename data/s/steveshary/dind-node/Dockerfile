FROM docker:17.05-git  
MAINTAINER Stephen Shary <stephen.shary@gmail.com>  
  
# Define commonly used variables  
ENV DOCKER_VERSION 17.05  
ENV COMPOSE_VERSION 1.14.0  
ENV NODE_VERSION 6.9.5  
  
# Install Java.  
RUN \  
apk add --no-cache --update \  
curl \  
py-pip \  
nodejs=6.9.5-r0 && \  
pip install docker-compose==1.14.0 && \  
rm -rf ~/.cache && \  
apk del py-pip && \  
rm -rf /var/cache/apk/*

