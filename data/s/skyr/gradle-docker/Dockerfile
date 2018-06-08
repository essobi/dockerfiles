FROM gradle:jdk-alpine  
  
MAINTAINER "Tom Pluess <tom@skyr.ch>"  
  
USER root  
  
RUN apk add \--update --no-cache \  
openssh-client curl openssl ca-certificates \  
git \  
docker \  
py-pip \  
&& update-ca-certificates \  
&& pip install --upgrade pip \  
&& pip install docker-compose  
  
ENV GRADLE_USER_HOME=/home/projects/sstate-cache/gradle  

