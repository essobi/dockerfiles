FROM alpine:edge  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk update \  
&& apk upgrade  
RUN apk add --no-cache php7 \  
php7-wddx \  
php7-snmp \  
php7-phar \  
php7-xmlreader \  
php7-fileinfo \  
php7-zip \  
php7-gd \  
php7-pdo_sqlite \  
php7-imap \  
php7-gmp \  
php7-bcmath \  
php7-enchant \  
php7-mysqli \  
php7-pear \  
php7-session \  
php7-xsl \  
php7-dom \  
php7-curl \  
php7-iconv \  
php7-gettext \  
php7-pdo_pgsql \  
php7-common \  
php7-json \  
php7-sysvsem \  
php7-calendar \  
php7-posix \  
php7-pdo \  
php7-tidy \  
php7-ldap \  
php7-pgsql \  
php7-pdo_mysql \  
php7-mbstring \  
php7-ctype \  
php7-pdo_dblib \  
php7-pcntl \  
php7-fpm \  
php7-bz2 \  
php7-openssl \  
php7-sysvshm \  
php7-ftp \  
php7-mcrypt \  
php7-intl \  
php7-pspell \  
php7-xmlrpc \  
php7-zlib \  
php7-xml \  
php7-sysvmsg \  
php7-opcache \  
php7-dba \  
php7-shmop \  
php7-mysqlnd \  
php7-sockets \  
php7-exif \  
php7-redis \  
php7-inotify \  
php7-gmagick \  
php7-uuid \  
php7-oauth \  
php7-memcached \  
php7-timezonedb \  
php7-lzf \  
php7-msgpack \  
php7-mailparse \  
php7-apcu  
RUN pear install Net_LDAP2  
RUN apk add --no-cache busybox-suid \  
nano \  
bash \  
sudo  
RUN rm -rf \  
/usr/share/doc \  
/usr/share/man \  
/tmp/* \  
/var/cache/apk/*  
WORKDIR /srv  
CMD php-fpm7 -D \  
&& crond -d 2 -f  
  

