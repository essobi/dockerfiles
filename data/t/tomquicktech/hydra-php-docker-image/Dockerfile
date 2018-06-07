FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y libmcrypt-dev zlib1g-dev  
RUN apt-get install -y vim cron supervisor  
RUN docker-php-ext-install mbstring pdo_mysql tokenizer  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN docker-php-ext-install zip  
  
CMD printenv | grep -v "no_proxy" >> /etc/environment  
  
CMD supervisord -c /etc/supervisor/supervisord.conf && supervisorctl reload &&
php-fpm

