FROM php:7.0-fpm-alpine  
  
ADD bin/* /usr/local/bin/  
  
RUN set -ex \  
&& ( \  
docker-php-ext-install pdo_mysql \  
) \  
&& ( \  
apk add \  
\--update \  
\--no-cache \  
icu-dev \  
&& docker-php-ext-configure intl --enable-intl \  
&& docker-php-ext-install intl \  
) \  
&& ( \  
apk add \  
\--no-cache \  
curl \  
curl-dev \  
&& docker-php-ext-configure curl --enable-curl \  
&& docker-php-ext-install curl \  
) \  
&& ( \  
apk add \  
\--no-cache \  
freetype \  
libpng \  
libjpeg-turbo \  
freetype-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
) \  
&& ( \  
apk add \  
\--no-cache \  
libxslt \  
libxslt-dev \  
&& docker-php-ext-configure xsl --enable-xsl \  
&& docker-php-ext-install xsl \  
) \  
&& ( \  
docker-php-ext-configure zip --enable-zip \  
&& docker-php-ext-install zip \  
) \  
&& ( \  
docker-php-ext-configure simplexml --enable-simplexml \  
&& docker-php-ext-install simplexml \  
) \  
&& ( \  
docker-php-ext-configure soap --enable-soap \  
&& docker-php-ext-install soap \  
) \  
&& ( \  
apk add \  
\--no-cache \  
libmcrypt-dev \  
libmcrypt \  
&& docker-php-ext-configure mcrypt \  
\--with-mcrypt \  
&& docker-php-ext-install mcrypt \  
) \  
&& ( \  
apk add \  
curl \  
&& curl -sSL https://phar.phpunit.de/phpunit.phar -o phpunit.phar \  
&& chmod +x phpunit.phar \  
&& mv phpunit.phar /usr/local/bin/phpunit \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php composer-setup.php --install-dir=/usr/local/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');" \  
# && curl -sSL https://files.magerun.net/n98-magerun.phar -o n98-magerun.phar
\  
# && chmod +x n98-magerun.phar \  
# && mv n98-magerun.phar /usr/local/bin/n98-magerun \  
) \  
&& ( \  
apk add \  
\--no-cache \  
g++ \  
make \  
autoconf \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& docker-php-source delete \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_port=9090" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_handler=dbgp" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
) \  
&& ( \  
apk add \  
\--no-cache \  
ssmtp \  
) \  
&& ( \  
addgroup \  
-g 101 \  
-S nginx \  
&& adduser \  
-u 101 \  
-D \  
-S \  
-G nginx nginx \  
)  
  
ENV SSMTP_HOST "mail:1025"  
  
ENTRYPOINT ["/usr/local/bin/docker-environment"]  

