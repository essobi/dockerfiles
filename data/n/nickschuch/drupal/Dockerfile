FROM php:7.0-apache  
MAINTAINER nick_schuch  
  
ENV VERSION 8.0.1  
# PHP.  
RUN apt-get update && apt-get install -y mysql-client libpng-dev libmcrypt-dev  
RUN docker-php-ext-install pdo pdo_mysql mcrypt gd mbstring opcache  
  
# Apache.  
RUN a2enmod rewrite  
  
# Drush.  
RUN curl -O http://files.drush.org/drush.phar  
RUN mv drush.phar /usr/local/bin/drush && chmod +x /usr/local/bin/drush  
  
# aGov.  
RUN cd /tmp && curl
http://ftp.drupal.org/files/projects/drupal-${VERSION}.tar.gz | tar xvz  
RUN rm -fR /var/www/html && mv /tmp/drupal-${VERSION} /var/www/html  
RUN mkdir -p /var/www/html/sites/default/files/tmp
/var/www/html/sites/default/private  
ADD settings.php /var/www/html/sites/default/settings.php  
ADD settings.config.php /var/www/html/sites/default/settings.config.php  
ADD services.yml /var/www/html/sites/default/services.yml  

