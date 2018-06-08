FROM php:7.1-cli  
RUN apt-get update \  
&& apt-get install -y software-properties-common git zip libpq-dev \  
&& docker-php-ext-install -j$(nproc) pdo_mysql \  
&& pecl install xdebug \  
&& echo "memory_limit = 12800M" >> /usr/local/etc/php/conf.d/666-custom.ini  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/ \  
&& ln -s /usr/local/bin/composer.phar /usr/local/bin/composer  

