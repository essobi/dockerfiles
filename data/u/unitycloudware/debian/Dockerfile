FROM debian:jessie  
MAINTAINER UCW Industries Ltd. <info@unitycloudware.com>  
  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install net-tools && \  
apt-get -y install iputils-ping && \  
apt-get -y install telnet && \  
apt-get -y install wget && \  
apt-get -y install curl && \  
apt-get -y install nano && \  
apt-get autoclean && \  
rm -rf /tmp/* && \  
rm -rf /var/log/*

