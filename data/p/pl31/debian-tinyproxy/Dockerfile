FROM pl31/debian:jessie  
MAINTAINER Patrick Büch <dh@paco.pl31.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install \  
tinyproxy  
  
EXPOSE 8888  
  
CMD service tinyproxy start && tail -f /var/log/tinyproxy/tinyproxy.log  

