FROM php:7.1  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q \  
&& apt-get install unzip git -y --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
COPY ./docker/php/php-prod.ini /usr/local/etc/php/php.ini  
COPY . /code  
  
WORKDIR /code  
  
RUN composer install --prefer-dist --no-interaction  
  
CMD php ./src/app.php run /data

