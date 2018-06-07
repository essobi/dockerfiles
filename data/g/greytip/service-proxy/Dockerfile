FROM haproxy:1.6.2  
MAINTAINER Sayeed Anjum <sayeed@greytip.com>  
  
COPY haproxy.cfg /etc/haproxy/haproxy.cfg  
COPY configure.sh /configure.sh  
RUN chmod +x /configure.sh  
  
CMD ["/configure.sh"]  

