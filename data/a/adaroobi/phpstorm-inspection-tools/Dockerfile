FROM php:7.0-alpine  
  
LABEL maintainer adaroobi  
  
# Install PHP Code Sniffer  
RUN pear install PHP_CodeSniffer  
  
# Install PHP Mess Detector  
RUN curl -o /usr/bin/phpmd.phar -L
http://static.phpmd.org/php/latest/phpmd.phar \  
&& chmod +x /usr/bin/phpmd.phar  
  
# Install bz2 library as its required to install bz2 php extension  
RUN apk update \  
&& apk add bzip2-dev  
  
# Install PHPMD bz2 php extension inorder to make phpmd run  
RUN docker-php-ext-install bz2 \  
&& rm -rf /var/cache/apk/*

