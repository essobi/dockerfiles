FROM php:7.0-fpm-alpine  
  
ENV PUID 1000  
ENV GUID 1000  
ENV APP_DATETIME Europe/Paris  
ENV APP_POST_SIZE 64M  
ENV APP_MEMORY_LIMIT 256M  
ENV APP_MAX_EXECUTION_TIME 120  
ENV APP_ENV development  
  
# bash  
RUN apk add --update --no-cache bash  
  
# install extensions  
# intl, zip, soap  
RUN apk add --update --no-cache libintl icu icu-dev libxml2-dev \  
&& docker-php-ext-install intl zip soap  
  
# mysqli, pdo, pdo_mysql, pdo_pgsql  
RUN apk add --update --no-cache postgresql-dev \  
&& docker-php-ext-install mysqli pdo pdo_mysql  
  
# mcrypt, gd, iconv  
RUN apk add --update --no-cache \  
freetype-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
&& docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j"$(getconf _NPROCESSORS_ONLN)" gd  
  
# gmp  
RUN apk add --update --no-cache gmp gmp-dev \  
&& docker-php-ext-install gmp  
  
# php-redis  
ENV PHPREDIS_VERSION 3.1.6  
RUN docker-php-source extract \  
&& curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz \  
&& tar xfz /tmp/redis.tar.gz \  
&& rm -r /tmp/redis.tar.gz \  
&& mv phpredis-$PHPREDIS_VERSION /usr/src/php/ext/redis \  
&& docker-php-ext-install redis \  
&& docker-php-source delete  
  
# apcu  
RUN docker-php-source extract \  
&& apk add --no-cache --virtual .phpize-deps-configure $PHPIZE_DEPS \  
&& pecl install apcu \  
&& docker-php-ext-enable apcu \  
&& apk del .phpize-deps-configure \  
&& docker-php-source delete  
  
# git client  
RUN apk add --update --no-cache git  
  
# imagick  
RUN apk add --update --no-cache autoconf g++ imagemagick-dev libtool make
pcre-dev \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& apk del autoconf g++ libtool make pcre-dev  
  
# Mongodb  
ENV PHPMONGODB_VERSION 1.4.1  
RUN apk add --update --no-cache autoconf g++ make pcre-dev \  
&& pecl install mongodb-$PHPMONGODB_VERSION \  
&& docker-php-ext-enable mongodb \  
&& apk del autoconf g++ make pcre-dev  
  
# install bcmath extension  
RUN docker-php-ext-install bcmath  
  
# Configure PHP  
RUN printf "[Date]\ndate.timezone = \"${APP_DATETIME}\"" >
/usr/local/etc/php/conf.d/zz-timezone.ini \  
&& echo "upload_max_filesize = ${APP_POST_SIZE}" >
/usr/local/etc/php/conf.d/zz-limit.ini \  
&& echo "post_max_size = ${APP_POST_SIZE}" >> /usr/local/etc/php/conf.d/zz-
limit.ini \  
&& echo "memory_limit = ${APP_MEMORY_LIMIT}" >> /usr/local/etc/php/conf.d/zz-
limit.ini \  
&& echo "max_execution_time = ${APP_MAX_EXECUTION_TIME}" >>
/usr/local/etc/php/conf.d/zz-limit.ini \  
&& echo "display_errors = On" > /usr/local/etc/php/conf.d/zz-errors.ini \  
&& echo "log_errors = on" >> /usr/local/etc/php/conf.d/zz-errors.ini \  
&& echo "error_reporting = E_ALL | E_STRICT" >> /usr/local/etc/php/conf.d/zz-
errors.ini  
  
# composer  
RUN cd /usr/bin \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& ln -s composer.phar composer  
  
# shadow  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories \  
&& apk add --update --no-cache shadow  
  
# Change userid  
RUN usermod -u ${PUID} www-data && \  
groupmod -g ${GUID} www-data  

