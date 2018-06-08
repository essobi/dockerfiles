FROM debian:jessie  
  
MAINTAINER joan joan@inte.es  
  
RUN mkdir /var/www \  
&& mkdir /var/www/html \  
&& mkdir /var/www/logs \  
&& mkdir /var/www/cache \  
&& mkdir /var/www/certs \  
&& mkdir /var/www/conf \  
&& mkdir /var/www/backup \  
&& mkdir /var/www/tmp \  
&& chown -R www-data:www-data /var/www/*  
  
VOLUME ["/var/www","/var/lib/mysql"]  
  
CMD echo "Data-only"

