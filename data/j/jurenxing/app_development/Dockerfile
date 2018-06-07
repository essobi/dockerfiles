FROM jurenxing/app  
MAINTAINER Allan Sun <allan.sun@bricre.com>  
ENV APP_ENVIRONMENT=development  
  
RUN apt-get update && apt-get -yq install --no-install-recommends \  
php7.0-xdebug telnet net-tools host \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /var/www/back  
  
# php.ini settings  
COPY php.development.ini /etc/php/7.0/php.development.ini  
ADD ApacheConfig.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN chown -R www-data:www-data /var/www/back  
  
RUN ln -s /etc/php/7.0/php.development.ini
/etc/php/7.0/cli/conf.d/99-php_extra.ini && \  
ln -s /etc/php/7.0/php.development.ini
/etc/php/7.0/apache2/conf.d/99-php_extra.ini  

