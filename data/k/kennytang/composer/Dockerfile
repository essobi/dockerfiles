# Composer Docker Container  
FROM kennytang/composer:base-php5  
MAINTAINER Kenny Tang <kenny.tang@icloud.com>  
  
ENV COMPOSER_VERSION 1.0.3  
# Install Composer  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php  
  
# Display version information.  
RUN composer --version  

