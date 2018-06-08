FROM ubuntu:latest  
MAINTAINER Marc Melvin <mmelvin@smartprocure.us>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends build-essential software-
properties-common python-software-properties curl wget git-core ca-
certificates nano ssh supervisor && \  
apt-get clean && \  
curl https://get.docker.io/builds/Linux/x86_64/docker-latest -o
/usr/local/bin/docker && \  
chmod +x /usr/local/bin/docker  
  
RUN locale-gen en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  

