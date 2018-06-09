FROM talentify/php-apache:base  
LABEL version="0.1.0"  
LABEL description="Image for development on Flux application."  
  
COPY xdebug.ini /tmp  
  
RUN pecl install xdebug-2.6.0 \  
&& docker-php-ext-enable xdebug \  
&& cat /tmp/xdebug.ini | grep -v '^#' >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini  

