FROM php:apache  
  
MAINTAINER Jeremy T. Bouse <Jeremy.Bouse@UnderGrid.net>  
  
COPY config/php.ini /usr/local/etc/php/  
COPY config/gpg-policy.conf /etc/apache2/conf-available/  
COPY src/ /var/www/html/  
  
RUN a2enmod rewrite && a2enconf gpg-policy  
  
HEALTHCHECK \--interval=5m --timeout=3s \  
CMD curl -fL http://localhost/ || exit 1  

