FROM ubuntu:14.04  
MAINTAINER jdorrance  
ENV ER="17.03.0-ce"  
  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
python3-pip \  
awscli  
  
RUN curl -L -o /tmp/docker-17.03.0-ce.tgz
https://get.docker.com/builds/Linux/x86_64/docker-17.03.0-ce.tgz && \  
tar -xz -C /tmp -f /tmp/docker-17.03.0-ce.tgz && \  
mv /tmp/docker/* /usr/bin && \  
curl -L https://github.com/docker/compose/releases/download/1.11.2/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \  
chmod +x /usr/local/bin/docker-compose  

