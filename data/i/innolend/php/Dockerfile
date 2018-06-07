FROM php:7.1.3-fpm-alpine  
  
# php-redis  
ENV PHPREDIS_VERSION 3.0.0  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN if [ ${PHP_TIMEZONE} ]; then \  
echo "date.timezone=${PHP_TIMEZONE}" > $PHP_INI_DIR/conf.d/date_timezone.ini \  
;fi  
  
RUN docker-php-source extract \  
&& curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz \  
&& tar xfz /tmp/redis.tar.gz \  
&& rm -r /tmp/redis.tar.gz \  
&& mv phpredis-$PHPREDIS_VERSION /usr/src/php/ext/redis \  
&& docker-php-ext-install redis \  
&& docker-php-source delete \  
# xdebug  
&& docker-php-source extract \  
&& apk add \--no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& apk del .phpize-deps-configure \  
&& docker-php-source delete \  
&& apk add --update --no-cache mysql-client git autoconf g++ imagemagick-dev
libtool make file gcc binutils isl libatomic libtool make re2c libstdc++
libgcc binutils-libs mpc1 mpfr3 gmp libgomp \  
&& apk add --update --no-cache coreutils libltdl openssl-dev libmcrypt-dev
curl-dev libc-dev musl-dev libxml2-dev icu-dev libedit-dev openssl-dev sqlite-
dev imagemagick-dev libjpeg-turbo-dev libpng-dev postgresql-dev freetype-dev
libmcrypt-dev icu-dev \  
&& pecl install imagick \  
&& mkdir /xhprof \  
&& mkdir /xhprof/output \  
&& chmod -R 777 /xhprof/output \  
&& cd /xhprof/ \  
&& git clone https://github.com/longxinH/xhprof \  
&& cd xhprof/extension \  
&& phpize \  
&& ./configure --with-php-config=/usr/local/bin/php-config \  
&& make && make install \  
&& docker-php-ext-enable imagick \  
&& apk del autoconf g++ libtool make \  
&& apk add --update --no-cache \  
git \  
graphviz \  
ttf-freefont \  
freetype-dev \  
libpng-dev libjpeg-turbo-dev \  
libmcrypt-dev \  
libintl icu icu-dev libxml2-dev \  
&& docker-php-ext-install intl zip soap pdo pdo_mysql opcache \  
&& docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& pear install pear/Image_GraphViz \  
&& docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" gd iconv mcrypt
bcmath \  
&& echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories \  
&& echo "@community http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk add --no-cache pdftk@community libgcj@edge autoconf bzip2 libbz2
bzip2-dev enchant  
  
RUN set -x && \  
# enable to use wget command for donwloading from https site  
apk add \--update --no-cache --virtual wget-dependencies \  
ca-certificates \  
openssl && \  
# tesseract is in testing repo  
echo 'http://dl-cdn.alpinelinux.org/alpine/v3.5/community' >>
/etc/apk/repositories && \  
apk add \--update --no-cache tesseract-ocr && \  
# download traineddata  
# english  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/eng.traineddata && \  
#german  
wget -q -P /usr/share/tessdata/ https://github.com/tesseract-
ocr/tessdata/raw/master/deu.traineddata && \  
# delete wget-dependencies  
apk del wget-dependencies  
  
COPY composer.json /opt/offline/composer.json  
COPY composer.lock /opt/offline/composer.lock  
  
# Install Code Sniffer  
RUN curl -sS https://getcomposer.org/installer | php -- \  
\--install-dir=/usr/bin \  
\--filename=composer \  
&& composer global require "squizlabs/php_codesniffer=*"  
  
COPY composer.json /opt/offline/composer.json  
  
RUN cd /opt/offline && composer install  
  
COPY ./xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
COPY ./opcache.ini /usr/local/etc/php/conf.d/opcache.ini  
  
ADD ./innolend.ini /usr/local/etc/php/conf.d/  
ADD ./innolend.pool.conf /usr/local/etc/php-fpm.d/  
  
EXPOSE 8001 18080  
WORKDIR /opt/project  
  
RUN rm -rf /var/cache/apk/*  
  
CMD ["php-fpm"]  

