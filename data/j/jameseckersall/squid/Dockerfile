FROM alpine:latest  
  
MAINTAINER James Eckersall <james.eckersall@gmail.com>  
  
RUN \  
apk update && \  
apk add apache2-utils bash curl squid  
  
ADD squid.conf /etc/squid/  
ADD entrypoint.sh /  
  
RUN \  
mkdir /var/spool/squid && \  
chmod -R 0777 /var/log/squid /etc/squid /var/spool/squid /var/run/squid  
  
ENV SQUID_USERNAME=squid \  
SQUID_PASSWORD=squid  
  
EXPOSE 3128  
  
USER squid  
  
ENTRYPOINT bash /entrypoint.sh  

