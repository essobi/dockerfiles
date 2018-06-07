FROM php:fpm  
MAINTAINER Diego Gullo <diego_gullo@bizmate.biz>  
  
# Install php extensions  
RUN apt-get update \  
&& apt-get install -y zlib1g-dev libicu-dev g++ libfreetype6-dev
libjpeg62-turbo-dev libpng12-dev libmcrypt-dev \  
&& pecl install xdebug \  
&& pecl install zip \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mbstring pdo pdo_mysql intl
opcache \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-enable xdebug \  
&& docker-php-ext-enable zip  
  
# Install Composer  
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-
setup.php \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'e115a8dc7871f15d853148a7fbac7da27d6c0030b848d9b3dc09e2a0388afed865e6a3d6b3c0fad45c48e2b5fc1196ae')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');"  
#Install blackfire probe  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so

