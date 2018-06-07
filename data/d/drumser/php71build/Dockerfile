FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
libreadline-dev \  
libcurl4-gnutls-dev \  
libxml2-dev \  
zlib1g-dev \  
libicu-dev \  
g++ \  
git  
RUN docker-php-ext-install pdo \  
pdo_mysql \  
mysqli \  
mcrypt \  
mbstring \  
bcmath \  
curl \  
soap \  
xml \  
intl  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar /usr/local/bin/composer  
  
RUN usermod -u 1000 www-data  
  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
# RUN chown -R www-data:www-data cont/var/cache  
# RUN chown -R www-data:www-data cont/var/logs  

