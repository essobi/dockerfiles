FROM ubuntu:xenial  
MAINTAINER Leandro Kollenberger <docker@kollenberger.me>  
  
RUN apt update && \  
apt install -y --no-install-recommends curl ca-certificates && \  
curl https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-
KEY.pub | apt-key add - && \  
echo 'deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial main'
> /etc/apt/sources.list.d/salt.list && \  
apt update && \  
apt install -y salt-master && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*  
  
EXPOSE 4505 4506  
ENTRYPOINT /usr/bin/salt-master  

