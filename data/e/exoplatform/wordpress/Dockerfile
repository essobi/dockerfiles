# Use apache for the moment. migrate to fpm later  
#FROM wordpress:4.6.1-php7.0-apache  
FROM php:7.0.14-fpm  
  
MAINTAINER eXo Platform <docker@exoplatform.com>  
  
ENV FPM_STATUS_ENABLED=true  
ENV FPM_PING_ENABLED=true  
ENV FPM_PROCESS_MANAGER=dynamic  
ENV FPM_MAX_CHILDREN=5  
ENV FPM_START_CHILDREN=2  
ENV FPM_MIN_SPARE_SERVERS=1  
ENV FPM_MAX_SPARE_SERVERS=3  
# Install wp command line  
RUN apt-get update && apt-get install -y less wget mysql-client sudo
imagemagick libmagickwand-dev && rm -rf /var/lib/apt/ && \  
cd /tmp && curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-
pages/phar/wp-cli.phar && \  
chmod +x wp-cli.phar && mv wp-cli.phar /usr/local/bin/wp && \  
docker-php-ext-install pdo_mysql && docker-php-ext-install mysqli && \  
pecl install imagick && \  
docker-php-ext-install gd  
  
ENTRYPOINT /entrypoint.sh  
  
ARG WORDPRESS_VERSION=4.6.6  
RUN chown www-data:www-data /var/www/html && sudo -u www-data wp core download
--version=${WORDPRESS_VERSION}  
  
COPY entrypoint.sh /  
RUN echo "extension=imagick.so" > /usr/local/etc/php/conf.d/imagick.ini  
RUN chmod a+x /entrypoint.sh  

