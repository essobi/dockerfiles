# minimal image to support php with mysql-client and lighttpd  
FROM lapax/buildroot:php  
MAINTAINER Lex Lapax <lexlapax@gmail.com>  
  
EXPOSE 80 443  
CMD ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

