FROM php:5.6-alpine  
MAINTAINER "The Impact Bot" <technology@bcorporation.net>  
  
RUN set -xe; \  
apk add --no-cache \  
libmemcached-dev \  
libmcrypt-dev \  
autoconf \  
g++ \  
make \  
postgresql-dev \  
cyrus-sasl-dev \  
build-base \  
readline-dev \  
openssl-dev \  
zlib-dev \  
libxml2-dev \  
glib-lang \  
wget \  
gnupg \  
ncurses \  
ca-certificates \  
readline \  
bzip2-dev \  
bash \  
libssl1.0 && \  
  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin && \  
  
# this version of alpine has postgresql 9.5 by default  
# TODO remove this dependency in the future  
wget http://ftp.postgresql.org/pub/source/v10.2/postgresql-10.2.tar.bz2 -O
/tmp/postgresql-10.2.tar.bz2 && \  
tar xvfj /tmp/postgresql-10.2.tar.bz2 -C /tmp && \  
cd /tmp/postgresql-10.2 && ./configure --enable-integer-datetimes --enable-
thread-safety --prefix=/usr/local --with-libedit-preferred --with-openssl &&
make world && make install world && make -C contrib install && \  
cd /tmp/postgresql-10.2/contrib && make && make install && \  
apk --purge del build-base wget gnupg ca-certificates && \  
rm -r /tmp/postgresql-10.2* && \  
# php extensions  
docker-php-ext-install \  
json \  
mcrypt \  
pdo \  
opcache \  
pcntl \  
bz2 \  
pdo_pgsql && \  
  
pecl install \  
xdebug-2.5.5 \  
memcached-2.2.0 && \  
  
docker-php-ext-enable xdebug memcached opcache pcntl && \  
# cleanup  
apk del \  
autoconf \  
g++ \  
make \  
cyrus-sasl-dev \  
readline-dev \  
openssl-dev \  
zlib-dev \  
libxml2-dev && \  
rm -rf /var/cache/apk/* && \  
docker-php-source delete && \  
rm -rf /tmp/*  
  
RUN mkdir -p /data/www  
  
VOLUME ["/data"]  
WORKDIR /data/www  
  
ADD php.ini $PHP_INI_DIR/conf.d/impact.ini  
ENTRYPOINT ["php"]  
CMD ["--help"]  

