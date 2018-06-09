FROM php:fpm-alpine  
  
ENV NR_AGENT_VERSION 6.4.0.163  
ENV NR_INSTALL_SILENT 1  
ENV NR_INSTALL_PHPLIST /usr/local/bin  
  
RUN apk add --no-cache --virtual .build-deps \  
freetype-dev \  
libjpeg-turbo-dev \  
postgresql-dev \  
libpng-dev \  
icu-dev \  
&& apk add --no-cache --virtual .required-deps \  
freetype \  
libjpeg-turbo \  
postgresql \  
libpng \  
icu-libs \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& docker-php-ext-install -j${NPROC} \  
gd \  
mysqli \  
opcache \  
pdo_pgsql \  
intl \  
pdo_mysql \  
&& curl
https://download.newrelic.com/php_agent/archive/$NR_AGENT_VERSION/newrelic-
php5-$NR_AGENT_VERSION-linux-musl.tar.gz | tar xz \  
&& newrelic-php5-$NR_AGENT_VERSION-linux-musl/newrelic-install install \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
RUN apk add --no-cache supervisor \  
&& rm -rf /var/cache/apk/*  
  
ENV NGINX_VERSION 1.10.1  
  
ENV GPG_KEYS B0F4253373F8F6F510D42178520A9993A1C052F8  
ENV CONFIG "\  
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
\--with-http_perl_module=dynamic \  
\--with-threads \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-http_slice_module \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-file-aio \  
\--with-http_v2_module \  
\--with-ipv6 \  
"  
  
RUN \  
addgroup -S nginx \  
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
perl-dev \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEYS" \  
&& gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure $CONFIG --with-debug \  
&& make \  
&& mv objs/nginx objs/nginx-debug \  
&& mv objs/ngx_http_xslt_filter_module.so objs/ngx_http_xslt_filter_module-
debug.so \  
&& mv objs/ngx_http_image_filter_module.so objs/ngx_http_image_filter_module-
debug.so \  
&& mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \  
&& mv objs/ngx_http_perl_module.so objs/ngx_http_perl_module-debug.so \  
&& ./configure $CONFIG \  
&& make \  
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
&& install -m755 objs/ngx_http_perl_module-debug.so
/usr/lib/nginx/modules/ngx_http_perl_module-debug.so \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& strip /usr/lib/nginx/modules/*.so \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/sbin/nginx /usr/lib/nginx/modules/*.so \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .nginx-rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /usr/src/nginx-$NGINX_VERSION \  
&& apk add --no-cache gettext \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY october /srv/app  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_VERSION 1.1.3  
ENV COMPOSER_SHA1 cdb416d7035c1f4032ba3058d6ec952e5d137005  
  
RUN mkdir -p \  
/srv/storage/main/app \  
/srv/storage/main/logs \  
&& rm -rf \  
/srv/app/storage/app \  
/srv/app/storage/logs \  
&& ln -sf /srv/storage/main/app /srv/app/storage/app \  
&& ln -sf /srv/storage/main/logs /srv/app/storage/logs  
  
VOLUME /srv/storage/main/app  
VOLUME /srv/storage/main/logs  
  
RUN apk add --no-cache --virtual .build-deps \  
git \  
unzip \  
curl \  
&& curl -o composer.phar
https://getcomposer.org/download/${COMPOSER_VERSION}/composer.phar \  
&& echo "$COMPOSER_SHA1 *composer.phar" | sha1sum -c - \  
&& php composer.phar global require "hirak/prestissimo:^0.3" \  
&& php composer.phar install -d /srv/app \  
&& rm composer.phar \  
&& rm -rf ~/.composer \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* \  
&& chown -R www-data:www-data /srv/app  
  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
COPY run.sh /srv/run.sh  
RUN mkdir /srv/app/public \  
&& chmod +x /srv/run.sh  
COPY october-config/* /srv/app/config/  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
COPY php-fpm.conf /usr/local/etc/php-fpm.d/zz-skiftet.conf  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY fastcgi_params /etc/nginx/fastcgi_params  
  
EXPOSE 80  
  
ENTRYPOINT ["/usr/bin/supervisord"]  
CMD ["-c", "/etc/supervisor/supervisord.conf"]  

