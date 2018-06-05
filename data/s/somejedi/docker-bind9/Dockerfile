FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install bind9  
ADD named.conf /etc/bind/named.conf  
ADD named.conf.options /etc/bind/named.conf.options  
EXPOSE 53  
VOLUME /data  
CMD ["/usr/sbin/named", "-c", "/etc/bind/named.conf", "-f"]  

