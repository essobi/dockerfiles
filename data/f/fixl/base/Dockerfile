FROM debian:stretch  
  
MAINTAINER Stefan Fuchs  
  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install apt-transport-https ca-certificates software-properties-
common curl gnupg && \  
curl -fsSL https://yum.dockerproject.org/gpg | apt-key add \- && \  
apt-key fingerprint 58118E89F3A912897C070ADBF76221572C52609D  
  
COPY docker.list /etc/apt/sources.list.d/docker.list  
  
RUN apt-get update && \  
apt-get install -y docker-engine && \  
apt-get clean autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  

