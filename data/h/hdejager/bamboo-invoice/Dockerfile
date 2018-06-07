FROM php:5.6-apache  
MAINTAINER Hannes de Jager <hannes.de.jager@gmail.com>  
  
ENV BASE_URL http://localhost/  
COPY web/ /var/www/html/  
RUN rm -f /var/www/html/img/logo/* && \  
mkdir /var/www/html/invoices_temp && \  
chown -R www-data:www-data /var/www/html  
  
# These files contains deployment specific configuration  
ONBUILD COPY database.php config.php email.php
/var/www/html/bamboo_system_files/application/config/  
ONBUILD COPY logo.* /var/www/html/img/logo/  
ONBUILD RUN chown -R www-data:www-data /var/www/html  
  
# 'apache2ctl -M' & 'php -m' on a server running bambooinvoice led me to this.  
RUN docker-php-ext-install mysql pdo_mysql  
  
VOLUME /var/www/html/invoices_temp  

