FROM nginx:stable  
MAINTAINER Sylvain Deloux <docker@eax.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/backports.list && \  
apt-get update && \  
apt-get install -y certbot -t jessie-backports && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/etc/apt/sources.list.d/backports.list  

