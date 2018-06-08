FROM php:7.0-cli  
  
MAINTAINER Sandae Macalalag <sandaemc@gmail.com>  
  
RUN apt-get update -y && \  
apt-get install -y \  
curl \  
git \  
zlib1g-dev \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
RUN docker-php-ext-install zip  
  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
RUN composer global require 'phpunit/phpunit=5.5.*'  
  
ENTRYPOINT ["/root/.composer/vendor/bin/phpunit"]  

