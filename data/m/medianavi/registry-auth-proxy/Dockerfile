# VERSION 1.0  
#  
FROM ubuntu:14.10  
MAINTAINER Igor Flederick <igor.flederick@mgo.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
apt-get update && \  
apt-get install -y apache2 && \  
rm -rf /var/lib/apt/lists/*  
RUN \  
a2enmod rewrite proxy_http headers  
  
ADD gateway.conf /etc/apache2/sites-enabled/000-default.conf  
  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
  
EXPOSE 80  

