FROM alpine  
  
MAINTAINER images@docker.li <images@docker.li>  
  
RUN apk add --no-cache --update bind  
  
EXPOSE 53/tcp 53/udp  
  
ENTRYPOINT ["/usr/sbin/named", "-f", "-u", "named", "-L",
"/var/log/named/named.log", "-c", "/etc/bind/named.conf", "-4", "-p", "53" ]

