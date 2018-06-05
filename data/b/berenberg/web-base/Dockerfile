FROM alpine:3.7  
  
COPY docker/ /  
  
ENV NGINX_VERSION=1.13.9 \  
PHP_VERSION=7.2.3 \  
PHPIZE_DEPS=" \  
autoconf \  
dpkg \  
dpkg-dev \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkgconf \  
re2c \  
"  
#  
# install php  
#  
RUN PHP_INI_DIR=/usr/local/etc/php \  
&& PHP_GPG_KEYS=1729F83938DA44E27BA0F4D3DBDB397470D12172\
B1B44D8F021E4E2D6021E995DC9FF8D3EE5AF27F \  
&&
PHP_URL="https://secure.php.net/get/php-${PHP_VERSION}.tar.xz/from/this/mirror"
\  
&&
PHP_ASC_URL="https://secure.php.net/get/php-${PHP_VERSION}.tar.xz.asc/from/this/mirror"
\  
&& PHP_CFLAGS="-fstack-protector-strong -fpic -fpie -O2" \  
&& PHP_CPPFLAGS="${PHP_CFLAGS}" \  
&& PHP_LDFLAGS="-Wl,-O1 -Wl,--hash-style=both -pie" \  
# ensure www-data user exists  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data \  
# create php conf dir  
&& mkdir -p $PHP_INI_DIR/conf.d \  
&& mkdir -p /var/run/php-fpm \  
# persistent deps  
&& apk add --no-cache --virtual .persistent-deps \  
ca-certificates \  
curl \  
tar \  
xz \  
# download php source  
&& set -xe \  
&& apk add --no-cache --virtual .fetch-deps \  
gnupg \  
# https://github.com/docker-library/php/issues/494  
libressl \  
&& mkdir -p /usr/src \  
&& cd /usr/src \  
&& wget -O php.tar.xz "${PHP_URL}" \  
&& wget -O php.tar.xz.asc "${PHP_ASC_URL}" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& for key in ${PHP_GPG_KEYS}; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys "$key" || \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys "$key" || \  
gpg --keyserver pgp.mit.edu --recv-keys "$key"; \  
done \  
&& gpg --batch --verify php.tar.xz.asc php.tar.xz \  
&& rm -rf "${GNUPGHOME}" \  
&& apk del .fetch-deps \  
# build deps  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
coreutils \  
curl-dev \  
libedit-dev \  
libressl-dev \  
libsodium-dev \  
libxml2-dev \  
sqlite-dev \  
&& export CFLAGS="${PHP_CFLAGS}" \  
CPPFLAGS="${PHP_CPPFLAGS}" \  
LDFLAGS="${PHP_LDFLAGS}" \  
# extract php source  
&& docker-php-source extract \  
&& cd /usr/src/php \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--with-config-file-path="${PHP_INI_DIR}" \  
\--with-config-file-scan-dir="${PHP_INI_DIR}/conf.d" \  
\--disable-cgi \  
# --enable-ftp is included here because ftp_ssl_connect() needs ftp to be
compiled statically (see https://github.com/docker-library/php/issues/236)  
\--enable-ftp \  
# --enable-mbstring is included here because otherwise there's no way to get
pecl to use it properly (see https://github.com/docker-library/php/issues/195)  
\--enable-mbstring \  
# --enable-mysqlnd is included here because it's harder to compile after the
fact than extensions are (since it's a plugin for several extensions, not an
extension in itself)  
\--enable-mysqlnd \  
# https://wiki.php.net/rfc/libsodium  
\--with-sodium \  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib \  
\  
# bundled pcre does not support JIT on s390x  
#
https://manpages.debian.org/stretch/libpcre3-dev/pcrejit.3.en.html#AVAILABILITY_OF_JIT_SUPPORT  
$(test "$gnuArch" = 's390x-linux-gnu' && echo '--without-pcre-jit') \  
\--enable-fpm \  
\--with-fpm-user=www-data \  
\--with-fpm-group=www-data \  
&& make -j "$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -perm +0111 -exec strip
--strip-all '{}' \+ || true; } \  
&& make clean \  
&& cd / \  
&& docker-php-source delete \  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --no-cache --virtual .php-rundeps $runDeps \  
# install the PHP extensions we need  
&& apk add --no-cache --virtual .build-deps \  
freetype-dev \  
icu-dev \  
imagemagick-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
libtool \  
&& export \  
CFLAGS="$PHP_CFLAGS" \  
CPPFLAGS="$PHP_CPPFLAGS" \  
LDFLAGS="$PHP_LDFLAGS" \  
&& pecl install \  
imagick \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-gd \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
&& docker-php-ext-configure intl \  
\--enable-intl \  
&& docker-php-ext-install \  
gd \  
intl \  
opcache \  
pdo_mysql \  
&& docker-php-ext-enable \  
imagick \  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive
/usr/local/lib/php/extensions \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --no-cache --virtual .php-ext-run-deps $runDeps \  
&& apk del .build-deps \  
# https://github.com/docker-library/php/issues/443  
&& pecl update-channels \  
&& rm -rf /tmp/pear ~/.pearrc \  
#  
# install nginx  
#  
&& NGINX_GPG_KEYS=B0F4253373F8F6F510D42178520A9993A1C052F8 \  
# add nginx user  
&& addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
# build deps  
&& apk add --no-cache --virtual .build-deps \  
curl \  
gcc \  
gd-dev \  
geoip-dev \  
gnupg \  
libc-dev \  
libressl-dev \  
libxslt-dev \  
linux-headers \  
make \  
pcre-dev \  
zlib-dev \  
&& curl -fSL https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz -o
nginx.tar.gz \  
&& curl -fSL https://nginx.org/download/nginx-${NGINX_VERSION}.tar.gz.asc -o
nginx.tar.gz.asc \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& found=''; \  
for server in \  
ha.pool.sks-keyservers.net \  
hkp://keyserver.ubuntu.com:80 \  
hkp://p80.pool.sks-keyservers.net:80 \  
pgp.mit.edu \  
; do \  
echo "Fetching GPG key ${NGINX_GPG_KEYS} from $server"; \  
gpg --keyserver "$server" \--keyserver-options timeout=10 \--recv-keys
"${NGINX_GPG_KEYS}" && found=yes && break; \  
done; \  
test -z "$found" && echo >&2 "error: failed to fetch GPG key
${NGINX_GPG_KEYS}" && exit 1; \  
gpg --batch --verify nginx.tar.gz.asc nginx.tar.gz \  
&& rm -rf "${GNUPGHOME}" nginx.tar.gz.asc \  
&& mkdir -p /usr/src \  
&& tar -zxC /usr/src -f nginx.tar.gz \  
&& rm nginx.tar.gz \  
&& cd /usr/src/nginx-${NGINX_VERSION} \  
&& ./configure \  
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
\--with-http_addition_module \  
\--with-http_flv_module \  
\--with-http_mp4_module \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-threads \  
\--with-stream \  
\--with-compat \  
\--with-file-aio \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& rm -rf /etc/nginx/html/ \  
&& mkdir -p /usr/share/nginx/html/ \  
&& install -m644 html/index.html /usr/share/nginx/html/ \  
&& install -m644 html/50x.html /usr/share/nginx/html/ \  
&& ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \  
&& strip /usr/sbin/nginx* \  
&& rm -rf /usr/src/nginx-${NGINX_VERSION} \  
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
&& apk add --no-cache --virtual .docker-healthcheck-deps fcgi \  
&& apk del .build-deps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
EXPOSE 80  
  
STOPSIGNAL SIGTERM  
  
HEALTHCHECK --interval=5s \--timeout=3s \--retries=2 \  
CMD \  
SCRIPT_NAME=/ping \  
SCRIPT_FILENAME=/ping \  
REQUEST_METHOD=GET \  
cgi-fcgi -bind -connect /var/run/fpm_socket || exit 1  
  
ENTRYPOINT ["docker-php-entrypoint"]  
  
CMD ["php-fpm"]  

