FROM alpine:3.6 as docker  
  
RUN apk add --no-cache curl  
RUN curl -Lo /tmp/docker.tgz
https://get.docker.com/builds/Linux/x86_64/docker-1.12.6.tgz  
RUN mkdir /tmp/docker  
RUN tar -xf /tmp/docker.tgz -C /tmp/docker  
  
FROM tazjin/kontemplate:1.3.0  
COPY \--from=docker /tmp/docker/docker/* /usr/local/bin/

