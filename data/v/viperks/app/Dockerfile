#  
# Basic Drupal 8 fpm container  
#  
FROM drupal:8-fpm  
  
VOLUME /var/www/html  
  
# Install the PHP extensions we need plus composer  
RUN apt-get update && apt-get install -y \  
ssh \  
&& pecl install xdebug \  
&& pecl install redis \  
&& docker-php-ext-enable \  
redis \  
&& curl -fsSL -o /usr/local/bin/phpunit "https://phar.phpunit.de/phpunit.phar"
\  
&& chmod +x /usr/local/bin/phpunit \  
&& apt-get -y clean \  
&& apt-get -y autoclean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/* || true \  
&& rm -rf && rm -rf /var/lib/cache/* && rm -rf /var/lib/log/* && rm -rf /tmp/*  
  
COPY php-fpm.conf /usr/local/etc/  
COPY php.ini /usr/local/etc/php/  

