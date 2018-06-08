FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y libmcrypt-dev  
RUN apt-get install -y vim cron supervisor git zip unzip  
  
RUN docker-php-ext-install mbstring pdo_mysql tokenizer  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN docker-php-ext-install bcmath  
  
# Install composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN mkdir -p /init  
  
WORKDIR /var/www/html  
  
EXPOSE 9000  
CMD supervisord -c /etc/supervisor/supervisord.conf && supervisorctl reload &&
php-fpm  

