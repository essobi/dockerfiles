FROM phusion/baseimage:0.9.21  
MAINTAINER rogueosb <rogueosb@gmail.com>  
  
RUN apt-get -qq update && \  
apt-get -qq install -y iproute2  
  
VOLUME ["/config"]  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Create template config file  
ADD duck.conf /root/duckdns/duck.conf  
  
RUN mkdir /etc/service/duckdns  
ADD duck.sh /etc/service/duckdns/run  
RUN chmod +x /etc/service/duckdns/run  

