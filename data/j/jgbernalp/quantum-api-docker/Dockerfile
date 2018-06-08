FROM php:fpm  
MAINTAINER Gabriel Bernal <josebernal@sanchobbdo.com>  
  
RUN apt-get update && \  
apt-get install -y php5-gd php5-mcrypt php5-mysql php-soap \  
php5-apcu php5-intl php5-xsl php5-common libxml2-dev \  
php5-gearman php5-mcrypt php5-memcache php5-imap php5-imagick php5-mongo
libssl-dev vim git nano  
  
RUN pecl install mongo  
RUN rm /usr/lib/php5/20131226/mongo.so  
RUN cp /usr/lib/php5/20131226/* /usr/local/lib/php/extensions/no-debug-non-
zts-20131226/  
RUN cp /etc/php5/mods-available/* /usr/local/etc/php/conf.d/  
RUN docker-php-ext-install mbstring  
  
RUN docker-php-ext-install soap  
  
ADD ./php.ini /usr/local/etc/php/  
  
CMD ["php-fpm"]  

