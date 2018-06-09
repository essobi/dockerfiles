FROM usijo/docker-php5fpm-trie_filter  
MAINTAINER Hongshun Yang<ojisucom@gmail.com>  
  
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN echo "@community http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
## support phpmyadmin  
RUN apk -U add php5-json php5-opcache php5-gd php5-mcrypt php5-mysqli
php5-pdo_mysql php5-apcu php5-ctype \  
php5-geoip@testing php5-imagick php5-memcached@testing php5-redis@testing
php5-xdebug@community \  
php5-curl php5-soap php5-openssl php5-gmp php5-dom php5-zip php5-bcmath
php5-xcache php5-gettext \  
php5-xmlreader php5-xmlrpc php5-bz2 php5-memcache php5-iconv php5-phar  
  
## support swoole - 2.0.7  
## support phalcon - 3.0.4  
ENV SWOOLE_VERSION 2.0.7  
ENV CPHALCON_VERSION 3.0.4  
ENV CPHALCON_DOWNLOAD_URL
https://github.com/phalcon/cphalcon/archive/v$CPHALCON_VERSION.tar.gz  
  
RUN apk add -U --virtual build-deps autoconf build-base php5-dev linux-headers
git \  
&& pecl install swoole-$SWOOLE_VERSION \  
&& cd /tmp/ \  
&& wget -qO- $CPHALCON_DOWNLOAD_URL | tar xvz \  
&& cd cphalcon-$CPHALCON_VERSION/build/ \  
&& ./install \  
&& cd ~ \  
&& rm -rf /tmp/* \  
&& apk del -U build-deps \  
&& rm -rf /var/cache/apk/*  
  
RUN echo "extension=swoole.so" > /etc/php5/conf.d/swoole.ini  
RUN echo "extension=phalcon.so" > /etc/php5/conf.d/phalcon.ini  
  
COPY tmpl/_etc_php5_php-fpm.conf.tmpl /etc/php5/php-fpm.conf.tmpl  
  
RUN dockerize -template "/etc/php5/php-fpm.conf.tmpl:/etc/php5/php-fpm.conf"  
  

