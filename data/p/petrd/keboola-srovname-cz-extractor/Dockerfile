FROM php:7.0  
MAINTAINER Sun Marketing, s.r.o. <developers@sunmarketing.cz>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install unzip git -y  
RUN cd && curl -sS https://getcomposer.org/installer | php && ln -s
/root/composer.phar /usr/local/bin/composer  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
  
ADD . /code  
  
RUN cd /code && composer install --prefer-dist --no-interaction  
  
WORKDIR /code  
  
CMD php ./src/run.php --data=/data

