# FPM, PHP 7.1, KickAssCommerce compatible container.  
FROM php:7.1-fpm  
  
MAINTAINER Adam Paterson <hello@adampaterson.co.uk>  
  
# Install PHP extension dependancies  
RUN apt-get update \  
&& apt-get install -y \  
libicu-dev \  
libmcrypt-dev \  
libxslt1-dev \  
zlib1g-dev  
  
# Install required PHP extensions  
RUN docker-php-ext-install \  
intl \  
mbstring \  
mcrypt \  
xsl \  
zip  
  
# Install PHP7 compatible version of xdebug  
RUN pecl install -o -f xdebug-2.5.0  
  
# Define volume for caching composer packages  
VOLUME /roo/.composer/cache  
  
# Add executables and config  
ADD bin/docker-environment /usr/local/bin/  
ADD etc/php.ini /usr/local/etc/php/conf.d/zz-kickass.ini  
ADD etc/php-xdebug.ini /usr/local/etc/php/conf.d/zz-xdebug.ini  
ADD etc/php-fpm.conf /usr/local/etc/  
  
# Define default environment variables  
ENV PHP_MEMORY_LIMIT 2G  
ENV PHP_ENABLE_XDEBUG false  
ENV APP_ROOT /var/www/kickass  
  
ENTRYPOINT ["/usr/local/bin/docker-environment"]  
CMD ["php-fpm", "-F"]  

