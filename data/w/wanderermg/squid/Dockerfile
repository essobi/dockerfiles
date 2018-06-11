FROM phusion/baseimage:0.9.16  
MAINTAINER Pavel Mironov <wanderermg@gmail.com>  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get update -y && \  
apt-get dist-upgrade -y && \  
apt-get install squid3 -y  
  
ADD squid.sh /etc/service/squid/run  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 3128  

