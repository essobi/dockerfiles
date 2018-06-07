FROM debian:jessie  
MAINTAINER Hellyna NG <hellyna@groventure.com>  
  
RUN export DEBIAN_FRONTEND='noninteractive' && \  
apt-get update && \  
apt-get install --no-install-recommends -y \  
nagios3-common && \  
apt-get autoremove -y && \  
apt-get clean -y && \  
rm -rvf /var/lib/apt/lists/* && \  
rm -rvf /var/tmp/* && \  
rm -rvf /tmp/*  

