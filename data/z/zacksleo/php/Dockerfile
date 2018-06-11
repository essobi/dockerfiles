FROM php:7.1-fpm-jessie  
  
ENV ACCEPT_EULA=Y  
  
# Microsoft SQL Server Prerequisites  
RUN apt-get update \  
&& curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \  
&& curl https://packages.microsoft.com/config/debian/8/prod.list \  
> /etc/apt/sources.list.d/mssql-release.list \  
&& apt-get install -y --no-install-recommends \  
locales \  
apt-transport-https \  
&& echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen \  
&& apt-get update \  
&& apt-get -y --no-install-recommends install msodbcsql unixodbc-dev  
  
RUN docker-php-ext-install mbstring \  
&& pecl install sqlsrv pdo_sqlsrv \  
&& docker-php-ext-enable sqlsrv pdo_sqlsrv  
  
  
# Install dependence for yii2  
RUN apt-get install -y curl libmcrypt-dev openssh-client zlib1g-dev git \  
&& docker-php-ext-install mcrypt zip \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_port=9000" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini  
  
# Install GD2  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  

