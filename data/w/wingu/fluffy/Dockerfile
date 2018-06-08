FROM php:7.2-fpm  
  
RUN apt-get update \  
&& apt-get install -y git zlib1g-dev unzip  
  
# core extensions  
RUN docker-php-ext-enable opcache  
RUN docker-php-ext-install bcmath \  
&& docker-php-ext-install zip  
  
ENV COMPOSER_HOME /var/www/composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN chown www-data:www-data $COMPOSER_HOME  
  
COPY src /fluffy/src  
COPY bin /fluffy/bin  
COPY composer.json /fluffy  
COPY composer.lock /fluffy  
RUN composer install --working-dir=/fluffy  
  
WORKDIR /app  
  
ENTRYPOINT ["php", "/fluffy/bin/fpr"]  

