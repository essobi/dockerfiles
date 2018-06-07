FROM haproxy:1.6.4-alpine  
  
MAINTAINER exira.com <info@exira.com>  
  
ADD haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg  
  
EXPOSE 9104  
CMD exec haproxy -db -f /usr/local/etc/haproxy/haproxy.cfg  

