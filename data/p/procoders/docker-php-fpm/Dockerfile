FROM php:7.2-fpm  
MAINTAINER Oleg Kopachovets <ok@procoders.tech>  
  
#install laravel requirements and aditional extensions  
RUN requirements="libmcrypt-dev g++ libicu-dev libmcrypt4 zlib1g-dev git
libcurl4-openssl-dev libfreetype6-dev libjpeg62-turbo-dev libpng-dev" \  
&& apt-get update && apt-get install -y $requirements \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install json \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install curl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install opcache  
  
#install Imagemagick & PHP Imagick ext  
RUN apt-get update && apt-get install -y \  
libmagickwand-dev --no-install-recommends  
  
RUN pecl install imagick && pecl install mcrypt-1.0.1 && docker-php-ext-enable
imagick && docker-php-ext-enable mcrypt  
  
#RUN requirementsToRemove="libmcrypt-dev g++ libicu-dev zlib1g-dev" \  
# && apt-get purge --auto-remove -y $requirementsToRemove \  
# && rm -rf /var/lib/apt/lists/*  
#install composer globally  
RUN curl -sSL https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
#replace default php-fpm config  
RUN rm -v /usr/local/etc/php-fpm.conf  
  
COPY config/php-fpm.conf /usr/local/etc/  
  
#add custom php.ini  
COPY config/php.ini /usr/local/etc/php/  
  
# Setup Volume  
VOLUME ["/var/www/"]  
  
#Set Workdir  
WORKDIR /var/www/  
  
#Add entrypoint  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["php-fpm"]  
  

