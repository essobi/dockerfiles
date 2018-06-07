FROM php:fpm-alpine  
  
MAINTAINER MrGeneral <mrgeneralgoo@gmail.com>  
  
# install depends  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache --virtual .persistent-deps \  
bash \  
git \  
bzip2-dev \  
gettext-dev \  
imap-dev \  
libaio-dev \  
libedit-dev \  
freetype-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
libxml2-dev \  
zlib-dev \  
libxslt-dev \  
icu-dev \  
# @see https://github.com/gliderlabs/docker-alpine/issues/341  
# openssl-dev \  
openldap-dev \  
bison \  
libvpx \  
openssh  
  
WORKDIR /tmp  
  
# install extensions  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
linux-headers \  
python \  
# install core extensions  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/lib --with-jpeg-
dir=/usr/lib --with-png-dir=/usr/lib --with-vpx-dir=/usr/lib \  
&& docker-php-ext-configure imap --with-imap --with-imap-ssl \  
&& docker-php-ext-configure exif --with-libdir=/usr/lib \  
&& docker-php-ext-configure mysqli --with-mysqli=mysqlnd \  
&& docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \  
&& docker-php-ext-configure zip --with-libdir=/usr/lib \  
&& docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" bz2 zip exif bcmath
sysvsem pcntl sockets pdo pdo_mysql mysqli intl readline soap xsl xmlrpc
gettext imap iconv \  
# install librdkafka  
&& curl -fsSL https://github.com/edenhill/librdkafka/archive/v0.11.3.tar.gz -o
librdkafka.tar.gz \  
&& mkdir -p librdkafka \  
&& tar -zxf librdkafka.tar.gz -C librdkafka --strip-components=1 \  
&& rm librdkafka.tar.gz \  
&& ( \  
cd librdkafka \  
&& ./configure \  
&& make -j"$(getconf _NPROCESSORS_ONLN)" \  
&& make install \  
) \  
&& rm -r librdkafka \  
# install ast  
&& curl -fsSL 'https://github.com/nikic/php-ast/archive/v0.1.6.tar.gz' -o php-
ast.tar.gz \  
&& mkdir -p php-ast \  
&& tar -xzf php-ast.tar.gz -C php-ast --strip-components=1 \  
&& rm php-ast.tar.gz \  
&& ( \  
cd php-ast \  
&& phpize \  
&& ./configure \  
&& make -j"$(getconf _NPROCESSORS_ONLN)" \  
&& make install \  
) \  
&& rm -r php-ast \  
&& docker-php-ext-enable ast \  
# install pecl extensions  
&& pecl install redis \  
&& pecl install rdkafka \  
&& pecl install swoole \  
&& pecl install xdebug \  
&& pecl install yaf \  
&& pecl install yac-beta \  
&& pecl install mongodb \  
&& docker-php-ext-enable redis rdkafka swoole yaf yac mongodb \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*  
  
#RUN apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing gnu-libiconv  
#ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php  
  
# install composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer \  
&& composer config -g repo.packagist composer
https://packagist.phpcomposer.com \  
&& rm -rf /tmp/*  

