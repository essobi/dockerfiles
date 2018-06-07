## A quick LAMP docker container for troubleshooting, experimenting, or
demonstrations  
##  
## DO NOT USE THIS IN PRODUCTION!!!!  
FROM greyltc/lamp  
MAINTAINER Aaron Saray <aaron@aaronsaray.com>  
  
## Turn on Display Errors  
RUN sed -i 's,display_errors = Off,display_errors = On,g' /etc/php/php.ini  
  
## Change Document Root  
RUN sed -i 's,DocumentRoot "/srv/http",DocumentRoot "/srv/http/public",g'
/etc/httpd/conf/httpd.conf  
RUN sed -i 's,<Directory "/srv/http">,<Directory "/srv/http/public">,g'
/etc/httpd/conf/httpd.conf  
  
## Move the info.php file to the public dir and create it  
RUN mkdir --parents /srv/http/public; mv /srv/http/info.php $_  

