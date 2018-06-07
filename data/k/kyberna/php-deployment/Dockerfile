FROM php:7.1  
MAINTAINER KYBERNA AG <info@kyberna.com>  
  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install
-y \  
git libcurl4-gnutls-dev libicu-dev libmcrypt-dev libvpx-dev libjpeg-dev
libpng-dev libxpm-dev \  
zlib1g-dev libfreetype6-dev libxml2-dev libexpat1-dev libbz2-dev libgmp3-dev
libldap2-dev unixodbc-dev \  
libpq-dev libsqlite3-dev libaspell-dev libsnmp-dev libpcre3-dev libtidy-dev
openssh-client rsync -y  
  
RUN docker-php-ext-install mcrypt pdo_mysql intl gd zip bz2 pcntl soap xml  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
RUN pecl install apcu  
RUN pecl install apcu_bc-1.0.3  
RUN pecl install xdebug  
RUN docker-php-ext-enable apcu --ini-name 10-docker-php-ext-apcu.ini  
RUN docker-php-ext-enable apc --ini-name 20-docker-php-ext-apc.ini  
RUN docker-php-ext-enable xdebug  
  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
RUN curl --location --output /usr/local/bin/phpcs
https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar && chmod +x
/usr/local/bin/phpcs  
RUN curl --location --output /usr/local/bin/phpmd
http://static.phpmd.org/php/latest/phpmd.phar && chmod +x /usr/local/bin/phpmd  
RUN curl --location --output /usr/local/bin/phpunit
https://phar.phpunit.de/phpunit.phar && chmod +x /usr/local/bin/phpunit  
  
COPY php.ini /usr/local/etc/php/  

