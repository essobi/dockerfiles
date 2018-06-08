FROM alpine:latest  
MAINTAINER HyperApp <HyperAppCloud@gmail.com>  
  
RUN apk --no-cache --update add squid>3.5.23-r0 curl apache2-utils  
  
RUN mkdir /usr/etc  
COPY squid.conf /etc/squid/squid.conf  
  
ENV PORT 3128  
ENV USERNAME hyperapp  
ENV PASSWORD hyperapp  
  
EXPOSE $PORT  
  
VOLUME /var/log/squid  
VOLUME /var/cache/squid  
VOLUME /var/spool/squid  
  
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["squid", "-N", "-d1"]  

