FROM debian:wheezy  
  
MAINTAINER jeff@igneous.io  
  
RUN apt-get update && apt-get install -y aufs-tools ca-certificates curl git
iptables xz-utils  
  
ENV DOCKER_VERSION 1.3.1  
RUN curl -SL https://get.docker.io/builds/Linux/x86_64/docker-$DOCKER_VERSION
-o /usr/bin/docker \  
&& chmod +x /usr/bin/docker  
  
# Total hack since this is typically a client looking at the host  
ENV DOCKER_HOST tcp://172.17.42.1:2375  

