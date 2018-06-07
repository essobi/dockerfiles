# Composer Docker Container  
FROM composer/composer:base  
MAINTAINER Droptica <info@droptica.com>  
  
ENV COMPOSER_VERSION 1.3.2  
# Install Composer  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php  
  
# Display version information.  
RUN composer --version  

