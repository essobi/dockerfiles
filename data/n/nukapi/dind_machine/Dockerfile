FROM docker:latest  
RUN apk update && apk add curl openssh bash  
# docker-machine  
RUN curl -L
https://github.com/docker/machine/releases/download/v0.13.0/docker-
machine-`uname -s`-`uname -m` >/tmp/docker-machine  
RUN install /tmp/docker-machine /usr/local/bin/docker-machine  
RUN mkdir -p /root/.docker

