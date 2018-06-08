FROM php:latest  
  
LABEL description="PHPUnit configured for Laravel" \  
maintainer="Khoa Nguyen <khoa.tan.nguyen.96@gmail.com>"  
  
RUN apt-get update && apt-get install -y \  
git \  
libcurl4-gnutls-dev \  
libicu-dev \  
libvpx-dev \  
libjpeg-dev \  
libpng-dev \  
libxpm-dev \  
zlib1g-dev \  
libfreetype6-dev \  
libxml2-dev \  
libexpat1-dev \  
libbz2-dev \  
libgmp3-dev \  
libldap2-dev \  
unixodbc-dev \  
libpq-dev \  
libsqlite3-dev \  
libaspell-dev \  
libsnmp-dev \  
libpcre3-dev \  
libtidy-dev \  
openssh-client  
  
# Install PHP Extensions  
# pdo_mysql, intl, zip, opcache, and xdebug  
RUN docker-php-ext-install \  
pdo_mysql \  
intl \  
gd \  
zip \  
bz2 \  
opcache\  
&& pecl install \  
xdebug-2.5.0 \  
&& docker-php-ext-enable xdebug  
  
# Memory Limit  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
  
# Install wait-for-it  
RUN curl --location --output /usr/local/bin/wait-for-it.sh
https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
\  
&& chmod +x /usr/local/bin/wait-for-it.sh  
  
# Install PHPUnit 5.7.9  
RUN curl --silent --show-error --location --output /usr/local/bin/phpunit
https://phar.phpunit.de/phpunit-5.7.9.phar \  
&& chmod +x /usr/local/bin/phpunit  
  
# Allow Composer to be run as root  
ENV COMPOSER_ALLOW_SUPERUSER 1  
# Install Composer  
RUN curl --silent --show-error https://getcomposer.org/installer | php --
--install-dir=/usr/local/bin --filename=composer  

