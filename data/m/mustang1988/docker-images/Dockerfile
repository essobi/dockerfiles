FROM php:7.1.6-fpm-alpine  
ENV NGINX_VERSION 1.12.0  
# install php exts  
COPY instantclient-basic-linux.x64-12.2.0.1.0.zip ./  
COPY instantclient-sdk-linux.x64-12.2.0.1.0.zip ./  
ENV LD_LIBRARY_PATH /usr/lib/oracle/12.2/client64/lib/:$LD_LIBRARY_PATH  
RUN apk update \  
&& apk add --no-cache --virtual .phpdeps \  
$PHPIZE_DEPS openssl-dev pcre-dev libpng-dev freetype-dev libjpeg-turbo-dev
libpng-dev libxml2-dev tzdata \  
&& apk add --no-cache libaio libmcrypt-dev libaio-dev \  
&& mkdir -p /usr/lib/oracle/12.2/client64/ \  
&& unzip instantclient-basic-linux.x64-12.2.0.1.0.zip -d
/usr/lib/oracle/12.2/client64/ \  
&& unzip instantclient-sdk-linux.x64-12.2.0.1.0.zip -d
/usr/lib/oracle/12.2/client64/ \  
&& mv /usr/lib/oracle/12.2/client64/instantclient_12_2
/usr/lib/oracle/12.2/client64/lib \  
&& ln -s /usr/lib/oracle/12.2/client64/lib/libclntsh.so.12.1
/usr/lib/oracle/12.2/client64/lib/libclntsh.so \  
&& pecl channel-update pecl.php.net \  
&& pecl install mongodb \  
&& pecl install redis \  
&& docker-php-ext-install opcache bcmath exif mcrypt mysqli pdo_mysql shmop
soap sockets sysvsem xmlrpc zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-png-
dir=/usr/include/ \--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-enable opcache bcmath exif gd mcrypt mysqli pdo_mysql shmop
soap sockets sysvsem xmlrpc zip mongodb redis \  
&& cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo "Asia/Shanghai" > /etc/timezone  
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
\--with-debug \  
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
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure $CONFIG \  
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
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
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
&& apk add --no-cache --virtual .gettext gettext \  
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
&& mv /tmp/envsubst /usr/local/bin/ \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& rm -rf /tmp/pear/* \  
&& rm -rf /var/cache/apk/* \  
&& rm -rf /etc/supervisord.conf \  
&& apk add --no-cache supervisor dcron  
#fix iconv  
RUN apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing gnu-libiconv \  
&& set -x \  
&& addgroup -g 555 -S www \  
&& adduser -u 555 -D -S -G www www \  
&& chmod -R 777 /run \  
&& chmod -R 777 /var \  
&& chmod -R 777 /usr/sbin \  
&& php -m  
ENV LD_PRELOAD /usr/lib/preloadable_libiconv.so php  
  
COPY supervisord.conf /etc/supervisord.conf  
  
COPY start.sh /start.sh  
  
EXPOSE 9001 80 443 9000  
  
  
ENTRYPOINT ["sh","/start.sh"]

