FROM php:5.6-fpm-alpine  
LABEL maintainer="bingo <bingov5@icloud.com>"  
  
###################################### NGINX
######################################  
  
ENV NGINX_VERSION 1.13.9  
  
RUN CONFIG="\  
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
libxslt-dev \  
gd-dev \  
geoip-dev \  
&& curl -fSL https://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure $CONFIG --with-debug \  
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
&& mkdir /app \  
&& install -m644 html/index.html /app \  
&& install -m644 html/50x.html /app \  
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
&& apk add --no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' /usr/sbin/nginx
/usr/lib/nginx/modules/*.so /tmp/envsubst \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --no-cache --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
&& apk add --no-cache tzdata \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY ./nginx/nginx.conf /etc/nginx/nginx.conf  
COPY ./nginx/nginx.vh.default.conf /etc/nginx/conf.d/default.conf  
  
EXPOSE 80  
  
STOPSIGNAL SIGTERM  
  
###################################### PHP-FPM
######################################  
  
# timezone  
ENV TIMEZONE Asia/Shanghai  
RUN apk add --no-cache tzdata \  
&& ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime \  
&& echo $TIMEZONE > /etc/timezone  
  
COPY ./php-fpm/php.ini /usr/local/etc/php/php.ini  
  
# mbstring opcache pdo mysql  
RUN docker-php-ext-install mbstring opcache pdo pdo_mysql mysql mysqli  
  
# gd zip  
RUN apk add --no-cache freetype libpng libjpeg-turbo freetype-dev libpng-dev
libjpeg-turbo-dev \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir \  
\--with-png-dir \  
\--with-jpeg-dir \  
\--with-zlib-dir \  
&& docker-php-ext-install -j${NPROC} gd zip \  
&& apk del freetype-dev libpng-dev libjpeg-turbo-dev  
  
# redis  
ENV PHPREDIS_VERSION 4.0.0RC1  
RUN apk add --no-cache curl \  
&& curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz \  
&& tar xfz /tmp/redis.tar.gz \  
&& rm -r /tmp/redis.tar.gz \  
&& mkdir -p /usr/src/php/ext \  
&& mv phpredis-$PHPREDIS_VERSION /usr/src/php/ext/redis \  
&& docker-php-ext-install redis \  
&& rm -rf /usr/src/php \  
&& apk del curl  
  
# mongo  
RUN apk update && apk add autoconf openssl-dev g++ make && \  
pecl install mongo && \  
docker-php-ext-enable mongo && \  
pecl install mongodb && \  
docker-php-ext-enable mongodb && \  
apk del --purge autoconf openssl-dev g++ make  
  
COPY ./php-fpm/docker-php-entrypoint /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/docker-php-entrypoint  
  
WORKDIR /app  
  
ENTRYPOINT ["docker-php-entrypoint"]  
  
CMD ["php-fpm"]  

