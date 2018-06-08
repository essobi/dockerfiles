FROM ubuntu:14.04  
MAINTAINER pomu0326@gmail.com  
  
RUN apt-get update \  
&& apt-get install -y git curl apparmor \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sSL https://get.docker.com/ubuntu/ | sh  
RUN curl -L https://github.com/docker/machine/releases/download/v0.4.1/docker-
machine_linux-amd64 > /usr/local/bin/docker-machine \  
&& chmod +x /usr/local/bin/docker-machine  
  
RUN curl -L https://github.com/docker/compose/releases/download/1.4.0/docker-
compose-Linux-x86_64 > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
  

