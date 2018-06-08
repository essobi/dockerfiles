FROM alpine:latest  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
RUN apk add --no-cache apache2 phpmyadmin php5-apache2  
  
RUN mkdir -p /run/apache2  
COPY phpmyadmin-config.inc.php /etc/phpmyadmin/config.inc.php  
COPY config-db.php /etc/phpmyadmin/config-db.php  
COPY run.sh /run.sh  
RUN sed -i 's#/var/www/localhost/htdocs#/usr/share/webapps/phpmyadmin#g'
/etc/apache2/httpd.conf  
RUN sed -i 's#ErrorLog logs/error.log#ErrorLog /dev/stderr#'
/etc/apache2/httpd.conf  
RUN sed -i 's#CustomLog logs/access.log combined#CustomLog /dev/stdout
combined#' /etc/apache2/httpd.conf  
RUN chown -R apache:apache /etc/phpmyadmin  
  
EXPOSE 80  
CMD ["/bin/sh", "/run.sh"]  

