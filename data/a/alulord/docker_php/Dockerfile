FROM php:7.2-fpm  
  
MAINTAINER Peter Simoncic <simoncic.p@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y \  
gettext-base \  
nano \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpq-dev \  
libmagickwand-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libssl-dev \  
libssl-doc \  
libsasl2-dev \  
zlib1g-dev \  
libicu-dev \  
&& docker-php-ext-install \  
bz2 \  
iconv \  
mbstring \  
mysqli \  
pdo_mysql \  
soap \  
intl \  
opcache \  
bcmath \  
zip  
RUN docker-php-ext-enable opcache soap bz2 iconv mbstring mysqli pdo_mysql
intl bcmath zip  
RUN docker-php-ext-install gd && docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
&& docker-php-ext-enable gd  
RUN pecl install mcrypt-1.0.1 && docker-php-ext-enable mcrypt  
RUN pecl install xdebug  
RUN pecl install apcu && docker-php-ext-enable apcu  
RUN pecl install mongodb && docker-php-ext-enable mongodb  
RUN pecl install redis && docker-php-ext-enable redis  
RUN yes '' | pecl install imagick && docker-php-ext-enable imagick  
  
#RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
# && curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
# && tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
# && mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
# && printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
# Install composer globally  
#RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/bin/ -  

