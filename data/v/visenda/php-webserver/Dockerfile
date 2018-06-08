FROM php:7.1.12-fpm-alpine  
  
MAINTAINER Adis Heric <adis.heric@visenda.com>  
  
ENV \  
# NGINX  
NGINX_VERSION="1.13.7" \  
NGINX_WEBROOT="/var/www/html" \  
NGINX_PROXY_FORWARD_HTTPS="0" \  
\  
# APP  
APP_ENV="dev" \  
APP_TIMEZONE="Europe/Berlin" \  
APP_FAKEMAIL_DIR="/fakemail" \  
\  
# SCRIPTS DIRS  
SCRIPTS_DIR="/scripts" \  
CUSTOM_SCRIPTS_DIR="/webserver-scripts" \  
\  
# PHP  
PHP_MEMORY_LIMIT="256M" \  
PHP_MAX_EXEC_TIME="60" \  
PHP_UPLOAD_MAX_FILESIZE="256M" \  
PHP_POST_MAX_SIZE="256M" \  
\  
# PHP-FPM  
PHP_FPM_PM="dynamic" \  
PHP_FPM_PM_MAX_CHILDREN="10" \  
PHP_FPM_PM_MAX_REQUESTS="500" \  
PHP_FPM_PM_START_SERVERS="4" \  
PHP_FPM_PM_MIN_SPARE_SERVERS="2" \  
PHP_FPM_PM_MAX_SPARE_SERVERS="6" \  
\  
# SMTP  
SMTP_HOSTNAME="smtp" \  
SMTP_PORT="587" \  
SMTP_FROM="it@visenda.com" \  
SMTP_USERNAME="visenda" \  
SMTP_PASSWORD="visenda" \  
SMTP_AUTH="1" \  
SMTP_TLS="1" \  
\  
# DB  
RDS_HOSTNAME="db" \  
RDS_DB_NAME="visenda" \  
RDS_USERNAME="visenda" \  
RDS_PASSWORD="visenda" \  
\  
# BUILD VARS  
LUA_MODULE_VERSION="0.10.11" \  
DEVEL_KIT_MODULE_VERSION="0.3.0" \  
LUAJIT_LIB="/usr/lib" \  
LUAJIT_INC="/usr/include/luajit-2.0" \  
# resolves #166 \  
LD_PRELOAD="/usr/lib/preloadable_libiconv.so php"  
  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk update \  
# install persistent deps  
&& apk add --no-cache \  
gnu-libiconv@testing \  
libxslt-dev \  
gd-dev \  
# install non-persistent build deps  
&& apk add --no-cache --virtual .build-deps \  
autoconf \  
gcc \  
libc-dev \  
make \  
openssl-dev \  
pcre-dev \  
zlib-dev \  
linux-headers \  
curl \  
gnupg \  
geoip-dev \  
perl-dev \  
luajit-dev \  
musl-dev \  
libffi-dev \  
augeas-dev \  
python-dev  
  
# configure + compile + install nginx  
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
\--with-http_perl_module=dynamic \  
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
\--add-module=/usr/src/ngx_devel_kit-$DEVEL_KIT_MODULE_VERSION \  
\--add-module=/usr/src/lua-nginx-module-$LUA_MODULE_VERSION \  
" \  
# add nginx user(1000) + group(1001)  
&& addgroup -S -g 1001 nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx -u 1000 nginx \  
# install nginx + modules  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz -o
nginx.tar.gz \  
&& curl -fSL http://nginx.org/download/nginx-$NGINX_VERSION.tar.gz.asc -o
nginx.tar.gz.asc \  
&& curl -fSL
https://github.com/simpl/ngx_devel_kit/archive/v$DEVEL_KIT_MODULE_VERSION.tar.gz
-o ndk.tar.gz \  
&& curl -fSL https://github.com/openresty/lua-nginx-
module/archive/v$LUA_MODULE_VERSION.tar.gz -o lua.tar.gz \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& found=''; \  
for server in \  
ha.pool.sks-keyservers.net \  
hkp://keyserver.ubuntu.com:80 \  
hkp://p80.pool.sks-keyservers.net:80 \  
pgp.mit.edu \  
; do \  
echo "Fetching GPG key $GPG_KEYS from $server"; \  
gpg --keyserver "$server" --keyserver-options timeout=10 --recv-keys
"$GPG_KEYS" && found=yes && break; \  
done; \  
test -z "$found" && echo >&2 "error: failed to fetch GPG key $GPG_KEYS" &&
exit 1; \  
gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -r "$GNUPGHOME" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& tar -zxC /usr/src -f ndk.tar.gz \  
&& tar -zxC /usr/src -f lua.tar.gz \  
&& rm nginx.tar.gz ndk.tar.gz lua.tar.gz \  
&& cd /usr/src/nginx-$NGINX_VERSION \  
&& ./configure $CONFIG --with-debug \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& mv objs/nginx objs/nginx-debug \  
&& mv objs/ngx_http_xslt_filter_module.so objs/ngx_http_xslt_filter_module-
debug.so \  
&& mv objs/ngx_http_image_filter_module.so objs/ngx_http_image_filter_module-
debug.so \  
&& mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \  
&& mv objs/ngx_http_perl_module.so objs/ngx_http_perl_module-debug.so \  
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
&& install -m755 objs/ngx_http_perl_module-debug.so
/usr/lib/nginx/modules/ngx_http_perl_module-debug.so \  
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
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
# install tools  
RUN apk add --no-cache \  
bash \  
supervisor \  
ca-certificates \  
msmtp \  
cyrus-sasl-dev  
  
# install php extensions + deps  
RUN apk add --no-cache \  
# mcrypt deps  
libmcrypt-dev \  
# intl deps  
icu-dev \  
# gd deps  
libpng-dev \  
freetype-dev \  
libjpeg-turbo-dev \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
# install php extensions  
&& docker-php-ext-install \  
pdo_mysql \  
mcrypt \  
gd \  
exif \  
intl \  
xsl \  
json \  
soap \  
dom \  
zip \  
opcache \  
mbstring \  
# clean up  
&& docker-php-source delete \  
&& mkdir -p \  
/etc/nginx \  
/run/nginx \  
/var/log/supervisor \  
# flush build-deps - not needed anymore  
&& apk del .build-deps  
  
# install resources  
COPY resources/entrypoint.sh /entrypoint.sh  
COPY resources/bin/* /usr/local/bin/  
COPY resources/scripts/ $SCRIPTS_DIR  
RUN chmod +x \  
$SCRIPTS_DIR/* \  
/usr/local/bin/* \  
/entrypoint.sh  
  
# prepare nginx  
RUN mkdir -p \  
/etc/nginx/sites-available/ \  
/etc/nginx/sites-enabled/ \  
/etc/nginx/ssl/ \  
&& rm -Rf /var/www/* \  
&& mkdir -p $NGINX_WEBROOT  
  
# install source files  
COPY src/ $NGINX_WEBROOT  
RUN chown -R 1000:1001 $NGINX_WEBROOT \  
&& chmod -R 775 $NGINX_WEBROOT  
  
# 443 not used initially but configurable via custom scripts  
EXPOSE 80 443  
  
CMD ["/entrypoint.sh"]  

