FROM php:7.1-fpm-alpine  
  
LABEL maintainer="runphp <runphp@qq.com>"  
  
ENV NGINX_VERSION 1.13.3  
# install nginx  
RUN GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 \  
&& CONFIG="\  
\--prefix=/etc/nginx \  
\--sbin-path=/usr/sbin/nginx \  
\--modules-path=/usr/lib/nginx/modules \  
\--conf-path=/etc/nginx/nginx.conf \  
\--error-log-path=/var/log/nginx/error.log \  
\--http-log-path=/var/log/nginx/access.log \  
\--pid-path=/var/run/nginx.pid \  
\--lock-path=/var/run/nginx.lock \  
\--http-client-body-temp-path=/var/cache/nginx/client_temp \  
\--http-proxy-temp-path=/var/cache/nginx/proxy_temp \  
\--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \  
\--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \  
\--http-scgi-temp-path=/var/cache/nginx/scgi_temp \  
\--user=nginx \  
\--group=nginx \  
\--with-http_ssl_module \  
\--with-http_realip_module \  
\--with-http_addition_module \  
\--with-http_sub_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_mp4_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_random_index_module \  
\--with-http_secure_link_module \  
\--with-http_stub_status_module \  
\--with-http_auth_request_module \  
\--with-http_xslt_module=dynamic \  
\--with-http_image_filter_module=dynamic \  
\--with-http_geoip_module=dynamic \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-stream_ssl_preread_module \  
\--with-stream_realip_module \  
\--with-stream_geoip_module=dynamic \  
\--with-http_slice_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-compat \  
\--with-file-aio \  
\--with-http_v2_module \  
" \  
&& addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
&& apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
curl \  
gnupg \  
libxslt-dev \  
gd-dev \  
geoip-dev \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& found=''; \  
for server in \  
ha.pool.sks-keyservers.net \  
hkp://keyserver.ubuntu.com:80 \  
hkp://p80.pool.sks-keyservers.net:80 \  
pgp.mit.edu \  
; do \  
echo "Fetching GPG key $GPG_KEYS from $server"; \  
gpg --keyserver "$server" \--keyserver-options timeout=10 --recv-keys
"$GPG_KEYS" && found=yes && break; \  
done; \  
test -z "$found" && echo >&2 "error: failed to fetch GPG key $GPG_KEYS" &&
exit 1; \  
gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure $CONFIG \--with-debug \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& mv objs/nginx objs/nginx-debug \  
&& mv objs/ngx_http_xslt_filter_module.so objs/ngx_http_xslt_filter_module-
debug.so \  
&& mv objs/ngx_http_image_filter_module.so objs/ngx_http_image_filter_module-
debug.so \  
&& mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \  
&& mv objs/ngx_stream_geoip_module.so objs/ngx_stream_geoip_module-debug.so \  
&& ./configure $CONFIG \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir /etc/nginx/conf.d/ \  
&& mkdir -p /var/www/html/ \  
&& install -m644 html/index.html /var/www/html/ \  
&& install -m644 html/50x.html /var/www/html/ \  
&& install -m755 objs/nginx-debug /usr/sbin/nginx-debug \  
&& install -m755 objs/ngx_http_xslt_filter_module-debug.so
/usr/lib/nginx/modules/ngx_http_xslt_filter_module-debug.so \  
&& install -m755 objs/ngx_http_image_filter_module-debug.so
/usr/lib/nginx/modules/ngx_http_image_filter_module-debug.so \  
&& install -m755 objs/ngx_http_geoip_module-debug.so
/usr/lib/nginx/modules/ngx_http_geoip_module-debug.so \  
&& install -m755 objs/ngx_stream_geoip_module-debug.so
/usr/lib/nginx/modules/ngx_stream_geoip_module-debug.so \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& strip /usr/lib/nginx/modules/*.so \  
&& rm -rf /usr/src/nginx-$NGINX_VERSION \  
\  
# Bring in gettext so we can get `envsubst`, then throw  
# the rest away. To do this, we need to install `gettext`  
# then move `envsubst` out of the way so `gettext` can  
# be deleted completely, then move `envsubst` back.  
&& apk add \--no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so
/tmp/envsubst \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
# add supervisor git bash openssl  
RUN apk --no-cache add supervisor git bash openssl  
  
RUN set -xe \  
&& apk --no-cache --virtual add linux-headers zlib-dev openssl-dev  
  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps autoconf g++ make pcre-dev re2c  
  
# install some extension  
RUN set -xe \  
&& apk add --no-cache --virtual libmcrypt-dev  
RUN docker-php-ext-install mcrypt  
  
RUN set -xe \  
&& apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev
libjpeg-turbo-dev \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
RUN set -xe \  
&& apk add --no-cache --virtual icu-dev  
RUN docker-php-ext-install intl  
  
RUN set -xe \  
&& apk add --no-cache --virtual libxslt-dev  
RUN docker-php-ext-install xsl  
  
RUN docker-php-ext-install bcmath  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install mysqli  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install soap  
  
# compile phalcon extension  
ENV PHALCON_VERSION=3.3.0  
RUN curl -fsSL
https://github.com/phalcon/cphalcon/archive/v${PHALCON_VERSION}.tar.gz -o
cphalcon.tar.gz \  
&& mkdir -p cphalcon \  
&& tar -xf cphalcon.tar.gz -C cphalcon --strip-components=1 \  
&& rm cphalcon.tar.gz \  
&& cd cphalcon/build \  
&& sh install \  
&& rm -rf cphalcon \  
&& docker-php-ext-enable phalcon  
  
# compile phpiredis extension  
RUN set -xe \  
&& apk --no-cache --virtual add hiredis-dev \  
&& curl -fsSL https://github.com/nrk/phpiredis/archive/v1.0.0.tar.gz -o
phpiredis.tar.gz \  
&& mkdir -p /tmp/phpiredis \  
&& tar -xf phpiredis.tar.gz -C /tmp/phpiredis --strip-components=1 \  
&& rm phpiredis.tar.gz \  
&& docker-php-ext-configure /tmp/phpiredis --enable-phpiredis \  
&& docker-php-ext-install /tmp/phpiredis \  
&& rm -r /tmp/phpiredis  
  
# compile swoole extension  
ENV SWOOLE_VERSION=2.0.10  
RUN set -xe \  
&& curl -fsSL http://pecl.php.net/get/swoole-${SWOOLE_VERSION}.tgz -o
swoole.tar.gz \  
&& mkdir -p /tmp/swoole \  
&& tar -xf swoole.tar.gz -C /tmp/swoole --strip-components=1 \  
&& rm swoole.tar.gz \  
&& docker-php-ext-configure /tmp/swoole --enable-swoole --enable-openssl
--enable-coroutine\  
&& docker-php-ext-install /tmp/swoole \  
&& rm -r /tmp/swoole  
  
ENV IGBINARY_VERSION=2.0.5  
RUN set -xe \  
&& curl -fsSL http://pecl.php.net/get/igbinary-${IGBINARY_VERSION}.tgz -o
igbinary.tar.gz \  
&& mkdir -p /tmp/igbinary \  
&& tar -xf igbinary.tar.gz -C /tmp/igbinary --strip-components=1 \  
&& rm igbinary.tar.gz \  
&& docker-php-ext-configure /tmp/igbinary --enable-igbinary \  
&& docker-php-ext-install /tmp/igbinary \  
&& rm -r /tmp/igbinary  
  
ENV MONGODB_VERSION=1.3.2  
# compile mongodb extension  
RUN set -xe \  
&& curl -fsSL http://pecl.php.net/get/mongodb-${MONGODB_VERSION}.tgz -o
mongodb.tar.gz \  
&& mkdir -p /tmp/mongodb \  
&& tar -xf mongodb.tar.gz -C /tmp/mongodb --strip-components=1 \  
&& rm mongodb.tar.gz \  
&& docker-php-ext-configure /tmp/mongodb --enable-mongodb \  
&& docker-php-ext-install /tmp/mongodb \  
&& rm -r /tmp/mongodb  
  
ENV MEMCACHED_VERSION=3.0.3  
# compile memcached extension  
RUN set -xe \  
&& apk add --no-cache zlib-dev libmemcached-dev cyrus-sasl-dev \  
&& curl -fsSL http://pecl.php.net/get/memcached-${MEMCACHED_VERSION}.tgz -o
memcached.tar.gz \  
&& mkdir -p /tmp/memcached \  
&& tar -xf memcached.tar.gz -C /tmp/memcached --strip-components=1 \  
&& rm memcached.tar.gz \  
&& docker-php-ext-configure /tmp/memcached --enable-memcached-igbinary
--enable-memcached \  
&& docker-php-ext-install /tmp/memcached \  
&& rm -r /tmp/memcached  
  
ENV REDIS_VERSION=3.1.4  
# compile redis extension  
RUN set -xe \  
&& curl -fsSL http://pecl.php.net/get/redis-${REDIS_VERSION}.tgz -o
redis.tar.gz \  
&& mkdir -p /tmp/redis \  
&& tar -xf redis.tar.gz -C /tmp/redis --strip-components=1 \  
&& rm redis.tar.gz \  
&& docker-php-ext-configure /tmp/redis --enable-redis \  
&& docker-php-ext-install /tmp/redis \  
&& rm -r /tmp/redis  
  
ENV APCU_VERSION=5.1.8  
# compile apcu extension  
RUN set -xe \  
&& curl -fsSL http://pecl.php.net/get/apcu-${APCU_VERSION}.tgz -o apcu.tar.gz
\  
&& mkdir -p /tmp/apcu \  
&& tar -xf apcu.tar.gz -C /tmp/apcu --strip-components=1 \  
&& rm apcu.tar.gz \  
&& docker-php-ext-configure /tmp/apcu --enable-apcu \  
&& docker-php-ext-install /tmp/apcu \  
&& rm -r /tmp/apcu  
  
ENV RAR_VERSION=4.0.0  
# compile rar extension  
RUN set -xe \  
&& curl -fsSL http://pecl.php.net/get/rar-${RAR_VERSION}.tgz -o rar.tar.gz \  
&& mkdir -p /tmp/rar \  
&& tar -xf rar.tar.gz -C /tmp/rar --strip-components=1 \  
&& rm rar.tar.gz \  
&& docker-php-ext-configure /tmp/rar --enable-rar \  
&& docker-php-ext-install /tmp/rar \  
&& rm -r /tmp/rar  
  
ENV IMAGICK_VERSION=3.4.3  
# compile imagick extension imagemagick-dev  
RUN set -xe \  
&& apk add --no-cache libtool imagemagick-dev \  
&& curl -fsSL http://pecl.php.net/get/imagick-${IMAGICK_VERSION}.tgz -o
imagick.tar.gz \  
&& mkdir -p /tmp/imagick \  
&& tar -xf imagick.tar.gz -C /tmp/imagick --strip-components=1 \  
&& rm imagick.tar.gz \  
&& docker-php-ext-configure /tmp/imagick --enable-imagick \  
&& docker-php-ext-install /tmp/imagick \  
&& rm -r /tmp/imagick  
  
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \  
&& echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
"$PHP_INI_DIR/conf.d/date_timezone.ini" \  
&& echo "output_buffering=4096" > "$PHP_INI_DIR/conf.d/output_buffering.ini"  
  
# add composer  
COPY install/composer.phar /usr/bin/composer  
RUN chmod a+x /usr/bin/composer  
  
# add phpunit  
COPY install/phpunit.phar /usr/bin/phpunit  
RUN chmod a+x /usr/bin/phpunit  
  
RUN mkdir -p /var/www \  
&& mkdir -p /etc/nginx/certs \  
&& mkdir -p /etc/nginx/conf.d  
  
VOLUME ["/var/www", "/etc/nginx/certs", "/etc/nginx/conf.d"]  
  
COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY etc/nginx/conf.d/_.conf /etc/nginx/conf.d/default.conf  
  
WORKDIR /var/www  
  
EXPOSE 80 443 9000  
STOPSIGNAL SIGTERM  
  
COPY etc/supervisor/conf.d/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

