FROM debian:jessie  
MAINTAINER jcoeltjen  
  
RUN apt-get update && \  
apt-get -y install squid3  
  
RUN /etc/init.d/squid3 stop  
  
COPY squid.conf /etc/squid3/squid.conf  
  
COPY start.sh /sbin/start.sh  
  
RUN chmod 755 /sbin/start.sh  
  
EXPOSE 3128  
CMD ["/sbin/start.sh"]  

