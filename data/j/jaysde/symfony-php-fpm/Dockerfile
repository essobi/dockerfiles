FROM php:7.1-fpm  
  
RUN apt-get update \  
&& apt-get install -y apt-utils \  
&& apt-get install -y git curl libicu-dev zlib1g-dev \  
&& docker-php-ext-install intl \  
&& pecl install apcu \  
&& docker-php-ext-enable apcu \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install zip \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer global require hirak/prestissimo \  
&& apt-get clean  
  
RUN usermod -u 1000 www-data  
  
ADD 60-user.ini /usr/local/etc/php/conf.d/  
  
WORKDIR /var/www/symfony/web  
  
EXPOSE 9000  
CMD ["php-fpm", "-F"]  

