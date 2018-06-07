FROM php:7.0-fpm  
MAINTAINER Kristen Garnier <garnier.kristen@icloud.com>  
  
  
RUN apt-get update \  
&& apt-get install -y \  
libicu-dev \  
zlib1g-dev \  
vim \  
git \  
ruby-full \  
xvfb \  
wget \  
wkhtmltopdf \  
# && curl -L -o /tmp/apcu-5.1.3.tgz https://pecl.php.net/get/apcu-5.1.3.tgz \  
# && tar xfz /tmp/apcu-5.1.3.tgz \  
# && mv apcu-5.1.3 /usr/src/php/ext/apcu \  
&& docker-php-ext-install \  
#apcu \  
intl \  
mbstring \  
mysqli \  
zip \  
pdo \  
pdo_mysql \  
&& php -r "readfile('https://getcomposer.org/installer');" | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& chmod +x /usr/local/bin/composer  
  
RUN usermod -u 1000 www-data  
  
COPY gestion/ /home/docker  
COPY php.ini /usr/local/etc/php/conf.d/custom.ini  
  
RUN mkdir /home/docker/web/image  
  
VOLUME ["/home/docker/web/image"]  
  
WORKDIR /home/docker  
  
#Set permissions to allow the app running smoothly  
RUN chmod -R 777 web app/cache app/logs web  
  
#Do some composer stuffs  
RUN composer install --prefer-source  

