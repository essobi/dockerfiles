FROM php:5.6-fpm  
  
MAINTAINER Ronan Pozzi <contact@treenity-web.fr>  
  
ENV PHP_MEMORY_LIMIT=512M \  
MAX_UPLOAD=50M \  
PHP_MAX_FILE_UPLOAD=200 \  
PHP_MAX_POST=100M \  
TIMEZONE=UTC  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libcurl4-nss-dev \  
php5-xdebug \  
php5-xhprof \  
php5-memcached \  
php5-redis \  
php5-pgsql \  
memcached \  
php5-memcache \  
ssmtp \  
php-soap \  
git \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install curl \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install json \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install opcache \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
RUN cp /usr/lib/php5/20131226/* /usr/local/lib/php/extensions/no-debug-non-
zts-20131226/ \  
&& cp /etc/php5/mods-available/* /usr/local/etc/php/conf.d  
  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install BlackFire agent  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
  
# Override ssmtp to mailhog  
RUN sed -i -e 's/mailhub=mail/mailhub=mailhog:1025/' /etc/ssmtp/ssmtp.conf  
  
# Copy override  
COPY ./php-ini-overrides.ini $PHP_INI_DIR/conf.d/99-overrides.ini  
  
VOLUME ['/var/www/html']  
  
RUN usermod -u 1000 www-data  
  
WORKDIR "/var/www/html"

