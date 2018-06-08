FROM alpine:latest  
  
RUN apk add --update \--no-cache squid  
COPY ./conf/squid.conf /etc/squid/conf/  
  
CMD /usr/sbin/squid -f /etc/squid/conf/squid.conf && sleep 1 && tail -f
/var/log/squid/access.log /var/log/squid/cache.log  

