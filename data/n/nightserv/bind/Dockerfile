#  
# Very simple bind container, based on alpine.  
#  
FROM alpine:latest  
MAINTAINER MrWorta <mrworta@nightsky.de>  
  
# Install updated and bind  
RUN apk update  
RUN apk add bind  
  
# Add default config:  
RUN /bin/cp /etc/bind/named.conf.authoritative /etc/bind/named.conf  
#  
# Talk to the real world  
VOLUME /etc/bind  
EXPOSE 53/udp  
EXPOSE 53/tcp  
  
#  
#  
ENTRYPOINT /bin/sh -c 'while true; do /usr/sbin/named -f -c
/etc/bind/named.conf; done'  

