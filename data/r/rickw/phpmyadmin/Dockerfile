FROM php:7.0-apache  
  
MAINTAINER Rick Wieman <git@rickw.nl>  
  
# Install extensions: gd, mysqli and mbstring  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev && rm -rf
/var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install mbstring  
  
# Fetch phpMyAdmin  
ENV PMA_VERSION 4.7.4  
RUN curl -LS
"https://files.phpmyadmin.net/phpMyAdmin/$PMA_VERSION/phpMyAdmin-$PMA_VERSION-
english.tar.gz" -o pma.tar.gz \  
&& tar xzf pma.tar.gz -C /var/www/html --strip-components=1 \  
&& rm pma.tar.gz  
  
# Add our configuration  
ADD config.inc.php /var/www/html/  
ADD php-upload_size.ini /usr/local/etc/php/conf.d/php-upload_size.ini  
  
# Remove unwanted files/folders  
RUN rm -rf /var/www/html/setup/ /var/www/html/examples/ /var/www/html/test/
/var/www/html/phpinfo.php  

