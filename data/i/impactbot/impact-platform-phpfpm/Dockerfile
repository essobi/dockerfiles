FROM php:5.6-fpm-alpine  
MAINTAINER "The Impact Bot" <technology@bcorporation.net>  
  
ENV PHANTOMJS_ARCHIVE="phantomjs.tar.gz"  
  
RUN set -xe; \  
echo http://dl-4.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories && \  
apk add --no-cache \  
libmemcached-dev \  
libmcrypt-dev \  
postgresql-dev \  
autoconf \  
g++ \  
make \  
cyrus-sasl-dev \  
shadow \  
imagemagick-dev \  
libtool \  
pcre-dev && \  
  
# php extensions  
docker-php-ext-install \  
json \  
mcrypt \  
pdo \  
pdo_pgsql \  
opcache \  
zip && \  
  
pecl install \  
xdebug \  
memcached-2.2.0 \  
imagick && \  
docker-php-ext-enable xdebug memcached opcache imagick && \  
  
# phantomjs prebuilt binary  
curl -Lk -o $PHANTOMJS_ARCHIVE https://github.com/fgrehm/docker-
phantomjs2/releases/download/v2.0.0-20150722/dockerized-phantomjs.tar.gz && \  
tar -xf $PHANTOMJS_ARCHIVE -C /tmp/ && \  
cp -R /tmp/etc/fonts /etc/ && \  
cp -R /tmp/lib/* /lib/ && \  
cp -R /tmp/lib64 / && \  
cp -R /tmp/usr/lib/* /usr/lib/ && \  
cp -R /tmp/usr/lib/x86_64-linux-gnu /usr/ && \  
cp -R /tmp/usr/share/* /usr/share/ && \  
cp /tmp/usr/local/bin/phantomjs /usr/bin/ && \  
rm -fr $PHANTOMJS_ARCHIVE /tmp/* && \  
# blackfire for profiling  
version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/alpine/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini && \  
# permissions  
usermod -u 1000 www-data && \  
# cleanup  
apk del \  
autoconf \  
g++ \  
make \  
cyrus-sasl-dev \  
shadow \  
libtool \  
pcre-dev && \  
rm -rf /var/cache/apk/* /tmp && \  
mkdir /tmp && \  
chmod 777 /tmp && \  
docker-php-source delete  
  
ADD php.ini $PHP_INI_DIR/conf.d/impact.ini  
  
EXPOSE 9000  
CMD ["php-fpm"]  

