FROM ubuntu:16.04  
MAINTAINER Jay Kline <jay@slushpupie.com>  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install bind9 make m4  
VOLUME /data  
RUN mkdir -p /data/etc  
RUN mv /etc/bind/ /data/ ; ln -s /data/etc /etc/bind  
EXPOSE 53  
CMD ["/usr/sbin/named", "-c", "/etc/bind/named.conf", "-f"]  

