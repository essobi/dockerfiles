FROM alpine:3.7  
LABEL maintainer="Leif Gensert <leif@leif.io>"  
  
RUN apk add --no-cache curl bash  
  
# Install Docker in Docker  
ENV DOCKER_VERSION="17.05.0-ce"  
RUN curl -L -o /tmp/docker-$DOCKER_VERSION.tgz
https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION.tgz \  
&& tar -xz -C /tmp -f /tmp/docker-$DOCKER_VERSION.tgz \  
&& mv /tmp/docker/* /usr/local/bin \  
&& rm -rf /tmp/*  
  
# Docker Cloud  
RUN apk -Uuv --no-cache add python py-pip  
  
ENV DOCKER_CLOUD_VERSION="1.0.9"  
RUN pip install docker-cloud==${DOCKER_CLOUD_VERSION}  

