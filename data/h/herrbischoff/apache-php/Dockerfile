## Base image  
FROM alpine  
  
## Maintainer info  
MAINTAINER Marcel Bischoff <marcel@herrbischoff.com>  
  
## Add experimental repository  
RUN echo http://nl.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
  
## Install Apache and PHP  
RUN apk add --update apache2 php-apache2 php-ctype php-pdo_mysql php-mysqli
php-zip php-xml php-zlib php-opcache php-pdo_odbc php-soap php-pgsql php-pdo
php-json php-mcrypt php-openssl php-gd php-curl shadow && \  
rm -rf /var/cache/apk/*  
  
## Change Apache UID  
RUN usermod -u 1000 apache  
  
## Remove PHP version exposure  
RUN sed -ir 's/expose_php = On/expose_php = Off/' /etc/php/php.ini  
  
## Copy modified httpd.conf into container  
COPY httpd.conf /etc/apache2/httpd.conf  
  
## Expose port  
EXPOSE 80  
## Set working directory  
WORKDIR /var/www/localhost/htdocs  
  
## Run Couchpotato  
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]  

