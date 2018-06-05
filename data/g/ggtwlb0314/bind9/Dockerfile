FROM ubuntu:14.04  
MAINTAINER Allen Wang <ggtwlb0314@gmail.com>  
  
RUN apt-get update && apt-get -y install bind9 && rm /etc/bind/*  
  
COPY etc/ /etc/bind/  
  
EXPOSE 53 53/udp  
  
CMD /usr/sbin/named -c /etc/bind/named.conf -f -g  
  

