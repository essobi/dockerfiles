FROM php:7.0.9-fpm  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY config/php.ini /usr/local/etc/php/  
COPY config/08-04-2016-php-browscap.ini /usr/local/etc/php/browscap.ini  
COPY config/www.conf /usr/local/etc/php-fpm.d/  
  
#IMPORTANT NO TABS IN THIS RUN COMMAND:  
RUN apt-get update && apt-get install -y nano zip supervisor libgmp-dev
libmcrypt-dev libfreetype6-dev libjpeg62-turbo-dev libpng12-dev zlib1g-dev
libxml2-dev libicu-dev libpq-dev \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install pdo_pgsql \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install bcmath \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& docker-php-ext-install gmp \  
## APCu  
&& pecl install apcu-5.1.5 \  
&& docker-php-ext-enable apcu  
  
  
#Set environment terminal to xterm to allow nano use:  
ENV TERM xterm-color  
  
WORKDIR /var/www/ea  
  
CMD ["/usr/bin/supervisord"]

