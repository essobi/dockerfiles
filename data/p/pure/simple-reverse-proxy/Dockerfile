FROM haproxy:alpine  
MAINTAINER Andrew Taranik <me@pureclouds.net>  
  
ADD haproxy.cfg.tmpl /usr/local/etc/haproxy/haproxy.cfg.tmpl  
ADD init.sh /init.sh  
  
EXPOSE 80  
RUN apk add --no-cache gettext \  
&& chmod +x /init.sh  
  
CMD ["/init.sh"]  

