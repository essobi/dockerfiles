FROM ubuntu:14.04  
MAINTAINER Bertrand Roussel <broussel@sierrawireless.com>  
  
ENV DOCKER_VERSION 1.5.0  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y vim-tiny cron rsyslog procps
wget  
  
RUN ( \  
wget -q -O /usr/bin/docker
https://get.docker.com/builds/Linux/x86_64/docker-$DOCKER_VERSION && \  
chmod +x /usr/bin/docker \  
)  
  
ADD entrypoint.sh /  
ADD clean.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

