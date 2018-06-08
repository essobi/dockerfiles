# Copyleft (ↄ) 2016 Thiago Almeida <thiagoalmeidasa@gmail.com>  
#  
# Distributed under terms of the GPLv2 license.  
  
FROM debian:8  
MAINTAINER Thiago Almeida <thiagoalmeidasa@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && \  
apt-get install -y git git-ftp openssh-client --no-install-recommends && \  
apt-get autoclean && apt-get --purge --yes autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["echo 'Use common git commands here.'"]  

