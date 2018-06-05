FROM birdsystem/app  
MAINTAINER Allan Sun <allan.sun@bricre.com>  
  
ENV APP_ENVIRONMENT=production  
  
ADD docker/app/php.production.ini /etc/php/7.0/php.production.ini  
ADD docker/app/ApacheConfig.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN ln -s /etc/php/7.0/php.production.ini /etc/php/7.0/cli/conf.d/zz-
php_extra.ini && \  
ln -s /etc/php/7.0/php.production.ini /etc/php/7.0/apache2/conf.d/zz-
php_extra.ini  
  
ADD wordpress /var/www/back  
RUN chown -R www-data:www-data /var/www/back  
WORKDIR /var/www/back  

