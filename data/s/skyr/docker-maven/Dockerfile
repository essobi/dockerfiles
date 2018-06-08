FROM maven:3.3-jdk-8-alpine  
  
MAINTAINER "Tom Pluess <tom@skyr.ch>"  
  
RUN apk add --update --no-cache \  
openssh-client curl openssl ca-certificates \  
git \  
docker \  
py-pip \  
&& update-ca-certificates \  
&& pip install --upgrade pip \  
&& pip install docker-compose  
  

