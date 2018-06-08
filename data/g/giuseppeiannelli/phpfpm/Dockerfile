FROM php:7.1.7-fpm-alpine  
LABEL maintainer "Giuseppe Iannelli <giuseppe.iannelli@mosaicoon.com>"  
LABEL description "php-fpm image with
exif,gd,mcrypt,mysqli,mongodb,pcntl,pdo_mysql,rdkafka,redis,ssh,soap,sockets,zip
modules and composer"  
  
### CUSTOM ENVIRONMENTS ###  
ENV APP_CWD=/app/code  
ENV PHP_MAXEXECUTIONTIME=30  
ENV PHP_MEMORYLIMIT=128M  
ENV PHP_DISPLAYERRORS=Off  
ENV PHP_DISPLASTARTUPERRORS=Off  
ENV PHP_ERRORREPORTING='E_ALL & ~E_DEPRECATED & ~E_STRICT'  
ENV PHP_VARIABLESORDER=GPCS  
ENV PHP_POSTMAXSIZE=8M  
ENV PHP_UPLOADMAXFILESIZE=2M  
ENV PHP_SHORTOPENTAG=Off  
  
# persistent / runtime deps  
RUN apk add --no-cache --virtual .persistent-deps \  
bison \  
freetype \  
libjpeg \  
libpng \  
libvpx \  
libldap \  
libmcrypt \  
bash \  
gettext \  
openssh  
  
#Install build dependences  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
coreutils \  
curl-dev \  
freetype-dev \  
libedit-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
openldap-dev \  
openssl-dev \  
sqlite-dev \  
git \  
python  
  
#install mcrypt pcntl soap sockets  
RUN $(which docker-php-ext-install) -j$(nproc) mcrypt pcntl soap sockets  
  
#configure and install exif  
RUN $(which docker-php-ext-configure) exif \  
\--with-libdir=/usr/lib \  
&& docker-php-ext-install -j$(nproc) exif  
  
#configure and install gd  
RUN $(which docker-php-ext-configure) gd \  
\--with-freetype-dir=/usr/lib/ \  
\--with-jpeg-dir=/usr/lib \  
\--with-png-dir=/usr/lib \  
\--with-vpx-dir=/usr/lib \  
&& docker-php-ext-install -j$(nproc) gd  
  
#configure and install msyqli  
RUN $(which docker-php-ext-configure) mysqli \  
\--with-mysqli=mysqlnd \  
&& docker-php-ext-install -j$(nproc) mysqli  
  
#configure and install pdo_mysql  
RUN $(which docker-php-ext-configure) pdo_mysql \  
\--with-pdo-mysql=mysqlnd \  
&& docker-php-ext-install -j$(nproc) pdo_mysql  
  
#configure and install zip  
RUN $(which docker-php-ext-configure) zip \  
\--with-libdir=/usr/lib \  
&& docker-php-ext-install -j$(nproc) zip  
  
#Install MongoDB Driver (http://php.net/manual/en/set.mongodb.php)  
RUN touch $PHP_INI_DIR/conf.d/mongodb.ini \  
&& pecl config-set php_ini $PHP_INI_DIR/conf.d/mongodb.ini \  
&& pear config-set php_ini $PHP_INI_DIR/conf.d/mongodb.ini \  
&& pecl install mongodb-1.2.9  
  
#Install redis PHP modules  
RUN touch $PHP_INI_DIR/conf.d/redis.ini \  
&& pecl config-set php_ini $PHP_INI_DIR/conf.d/redis.ini \  
&& pear config-set php_ini $PHP_INI_DIR/conf.d/redis.ini \  
&& pecl install redis-3.1.2  
  
# #Install SSH2 Driver (http://pecl.php.net/package/ssh2)  
# RUN touch $PHP_INI_DIR/conf.d/ssh.ini \  
# && pecl config-set php_ini $PHP_INI_DIR/conf.d/ssh.ini \  
# && pear config-set php_ini $PHP_INI_DIR/conf.d/ssh.ini \  
# && pecl install ssh2-1.0  
#Install librdkafka  
RUN cd /usr/src/ \  
&& git clone https://github.com/edenhill/librdkafka.git \  
&& cd librdkafka/ \  
&& git checkout tags/v0.9.5 \  
&& ./configure \  
&& make -j"$(getconf _NPROCESSORS_ONLN)" \  
&& make install \  
&& cd /usr/src/ \  
&& rm -rf /usr/src/librdkafka/  
  
#Install redis PHP modules  
RUN touch $PHP_INI_DIR/conf.d/kafka.ini \  
&& pecl config-set php_ini $PHP_INI_DIR/conf.d/kafka.ini \  
&& pear config-set php_ini $PHP_INI_DIR/conf.d/kafka.ini \  
&& pecl install rdkafka-3.0.3  
  
# #Install pthreads PHP modules if you use php-fpm zts  
# RUN touch /docker/configurations/php/conf.d/pthreads.ini \  
# && pecl config-set php_ini /docker/configurations/php/conf.d/pthreads.ini \  
# && pear config-set php_ini /docker/configurations/php/conf.d/pthreads.ini \  
# && pecl install pthreads-3.1.6  
RUN apk del .build-deps  
RUN rm -rf /var/cache/apk/*  
  
#install composer for PHP  
RUN curl -fSL https://getcomposer.org/composer.phar -o /usr/bin/composer &&
chmod +x /usr/bin/composer  
  
COPY docker /docker  
COPY docker-php-entrypoint /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-php-entrypoint  
  
#set workdir  
WORKDIR ${APP_CWD}  
  
ENTRYPOINT ["/usr/local/bin/docker-php-entrypoint"]  
CMD ["php-fpm"]  

