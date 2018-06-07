FROM php:7.2.1-fpm-alpine  
  
MAINTAINER Julien Neuhart <j.neuhart@thecodingmachine.com>  
  
# |--------------------------------------------------------------------------  
# | Main PHP extensions  
# |--------------------------------------------------------------------------  
# |  
# | Installs the main PHP extensions  
# |  
RUN apk add --no-cache --virtual .persistent-deps \  
libjpeg \  
libjpeg-turbo \  
libjpeg-turbo-dev \  
libpng \  
libpng-dev \  
freetype \  
freetype-dev \  
icu \  
icu-dev \  
#libmcrypt \  
#libmcrypt-dev \  
libxml2-dev \  
yaml-dev  
  
RUN set -xe &&\  
apk add --no-cache --virtual .build-deps &&\  
docker-php-ext-configure bcmath --enable-bcmath &&\  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ &&\  
docker-php-ext-configure intl --enable-intl &&\  
docker-php-ext-configure mbstring --enable-mbstring &&\  
#docker-php-ext-configure mcrypt --enable-mcrypt &&\  
docker-php-ext-configure pdo_mysql --with-pdo-mysql &&\  
docker-php-ext-configure opcache --enable-opcache &&\  
docker-php-ext-configure soap --enable-soap &&\  
docker-php-ext-configure zip --enable-zip &&\  
docker-php-ext-install \  
bcmath \  
gd \  
intl \  
mbstring \  
#mcrypt \  
pdo_mysql \  
opcache \  
soap \  
zip  
  
# Note: mycrpt is no more supported since PHP 7.2. See:
http://php.net/manual/fr/migration71.deprecated.php  
# |--------------------------------------------------------------------------  
# | APCu extension  
# |--------------------------------------------------------------------------  
# |  
# | Installs the APCu extension for PHP.  
# |  
ENV APCU_VERSION 5.1.9  
RUN mkdir -p /usr/src/php/ext/apcu &&\  
curl -L https://github.com/krakjoe/apcu/archive/v$APCU_VERSION.tar.gz | tar
xvz -C /usr/src/php/ext/apcu --strip 1 &&\  
echo 'apcu' >> /usr/src/php-available-exts &&\  
docker-php-ext-install apcu  
  
# |--------------------------------------------------------------------------  
# | PHP extension for Redis  
# |--------------------------------------------------------------------------  
# |  
# | Installs the Redis extension for PHP.  
# |  
ENV PHPREDIS_VERSION 3.1.6  
RUN mkdir -p /usr/src/php/ext/redis &&\  
curl -L https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz
| tar xvz -C /usr/src/php/ext/redis --strip 1 &&\  
echo 'redis' >> /usr/src/php-available-exts &&\  
docker-php-ext-install redis  
  
# |--------------------------------------------------------------------------  
# | 3.7 & Edge repositories  
# |--------------------------------------------------------------------------  
# |  
# | Installs the 3.7 and Edge repositories, as some packages are not available  
# | by default in the current version of Alpine used by the PHP image.  
# |  
RUN echo http://dl-cdn.alpinelinux.org/alpine/v3.7/main/ >>
/etc/apk/repositories &&\  
echo http://dl-cdn.alpinelinux.org/alpine/v3.7/community/ >>
/etc/apk/repositories &&\  
echo http://dl-cdn.alpinelinux.org/alpine/edge/main/ >> /etc/apk/repositories
&&\  
echo http://dl-cdn.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories  
  
# |--------------------------------------------------------------------------  
# | YAML extension  
# |--------------------------------------------------------------------------  
# |  
# | Installs the YAML extension for PHP.  
# |  
ENV YAML_VERSION 2.0.2  
RUN mkdir -p /usr/src/php/ext/yaml &&\  
curl -L https://github.com/php/pecl-file_formats-
yaml/archive/$YAML_VERSION.tar.gz | tar xvz -C /usr/src/php/ext/yaml --strip 1
&&\  
echo 'yaml' >> /usr/src/php-available-exts &&\  
docker-php-ext-install yaml  
  
# |--------------------------------------------------------------------------  
# | Xdebug  
# |--------------------------------------------------------------------------  
# |  
# | Installs Xdebug, a tool for easily debugging your PHP code.  
# |  
ENV XDEBUG_VERSION 2.6.0  
RUN mkdir -p /usr/src/php/ext/xdebug &&\  
curl -L https://github.com/xdebug/xdebug/archive/$XDEBUG_VERSION.tar.gz | tar
xvz -C /usr/src/php/ext/xdebug --strip 1 &&\  
echo 'xdebug' >> /usr/src/php-available-exts &&\  
docker-php-ext-install xdebug &&\  
{ \  
echo 'xdebug.remote_enable=on'; \  
echo 'xdebug.remote_autostart=off'; \  
echo 'xdebug.remote_port=9000'; \  
echo 'xdebug.remote_handler=dbgp'; \  
echo 'xdebug.remote_connect_back=0'; \  
} >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
  
# |--------------------------------------------------------------------------  
# | OpenSSL  
# |--------------------------------------------------------------------------  
# |  
# | Installs OpenSSL for wget command.  
# |  
ENV OPENSSL_VERSION 1.0.2n-r0  
  
RUN apk --no-cache add openssl=$OPENSSL_VERSION  
  
# |--------------------------------------------------------------------------  
# | Git  
# |--------------------------------------------------------------------------  
# |  
# | Installs Git command (useful for Composer).  
# |  
RUN apk --no-cache add git  
  
# |--------------------------------------------------------------------------  
# | Composer  
# |--------------------------------------------------------------------------  
# |  
# | Installs Composer to easily manage your PHP dependencies.  
# |  
ENV COMPOSER_VERSION 1.6.2  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=$COMPOSER_VERSION &&\  
chmod +x /usr/local/bin/composer  
  
# |--------------------------------------------------------------------------  
# | prestissimo  
# |--------------------------------------------------------------------------  
# |  
# | Installs prestissimo to fix Composer performance issues.  
# |  
# installs prestissimo for the www-data user.  
USER www-data  
  
ENV PRESTISSIMO_VERSION 0.3.7  
RUN composer global require hirak/prestissimo:$PRESTISSIMO_VERSION  
  
# done, let's go back to root user!  
USER root  
  
# |--------------------------------------------------------------------------  
# | PHP Coding Standards Fixer  
# |--------------------------------------------------------------------------  
# |  
# | The PHP Coding Standards Fixer tool fixes most issues in your code when  
# | you want to follow the PHP coding standards as defined in the PSR-1 and  
# | PSR-2 documents and many more.  
# |  
ENV PHP_CS_FIXER_VERSION 2.10.0  
RUN wget https://github.com/FriendsOfPHP/PHP-CS-
Fixer/releases/download/v$PHP_CS_FIXER_VERSION/php-cs-fixer.phar -O php-cs-
fixer &&\  
chmod a+x php-cs-fixer &&\  
mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
# |--------------------------------------------------------------------------  
# | NodeJS  
# |--------------------------------------------------------------------------  
# |  
# | Installs NodeJS and npm. The later will allow you to easily manage  
# | your frontend dependencies.  
# |  
ENV NODE_VERSION 8.9.4-r0  
  
RUN apk --no-cache add nodejs=$NODE_VERSION nodejs-npm=$NODE_VERSION  
  
# |--------------------------------------------------------------------------  
# | yarn  
# |--------------------------------------------------------------------------  
# |  
# | Installs yarn. It provides some nice improvements over npm.  
# |  
ENV YARN_VERSION 1.3.2-r0  
  
RUN apk --no-cache add yarn=$YARN_VERSION  
  
# |--------------------------------------------------------------------------  
# | Permissions issues workaround  
# |--------------------------------------------------------------------------  
# |  
# | Installs shadow package to enable usermod and groupmod command.  
# |  
RUN apk --no-cache add shadow

