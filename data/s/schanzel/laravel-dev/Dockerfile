FROM php:7.0-cli-stretch  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
# Install system packages  
RUN apt-get update \  
&& apt-get install -y \  
git \  
mysql-client \  
curl \  
libicu-dev \  
openssh-client \  
libmemcached-dev \  
libsasl2-dev \  
libmcrypt-dev \  
libxml2-dev \  
libfreetype6-dev \  
libpng-dev \  
libjpeg-dev \  
libpng-dev \  
zip \  
unzip  
  
# Install PHP extensions  
RUN docker-php-source extract \  
&& docker-php-ext-install iconv \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install opcache \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& pecl install memcached-3.0.0 \  
&& docker-php-ext-enable memcached \  
&& docker-php-source delete \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN mkdir -p /opt/code  
VOLUME /opt/code  
WORKDIR /opt/code  
  
EXPOSE 8000  
  
CMD bash -c "composer install --no-progress --no-scripts --no-suggest \  
&& php artisan serve --host 0.0.0.0 --port 8000"  

