FROM php:7-apache  
MAINTAINER Jonathan Plugaru <jplugaru@hotmail.fr>  
  
COPY default.conf /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');"  
  
RUN apt update && apt install -y \  
zip  
  
ADD api /var/www/api  
WORKDIR /var/www/api  
RUN rm -f web/index_dev.php  
RUN chown -R www-data:www-data var/logs var/cache  
  
RUN composer --no-dev -o install  

