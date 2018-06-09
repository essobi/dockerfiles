FROM ubuntu:latest  
MAINTAINER HE201408@students.ephec.be  
  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get install -y bind9  
RUN apt-get install -y dnsutils  
  
ENV DATA_DIR=/data/bind  
  
ADD start /start  
RUN chmod 755 /start  
  
EXPOSE 53/udp 53/tcp  
#VOLUME ["${DATA_DIR}"]  
CMD ["/start"]  
  
ADD named.conf.local /etc/bind/named.conf.local  
ADD db.wt14.ephec-ti.be /etc/bind/db.wt14.ephec-ti.be  
Run chmod -R 777 /etc/bind  

