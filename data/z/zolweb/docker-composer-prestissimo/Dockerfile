# Composer Docker Container  
FROM composer/composer:base  
MAINTAINER Rob Loach <robloach@gmail.com>  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /home/.composer  
ENV COMPOSER_VERSION 1.1.1  
RUN apt-get update && apt-get install -yyq sudo  
  
# Install Composer  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php  
  
RUN composer --version  
  
CMD []  
ENTRYPOINT []  

