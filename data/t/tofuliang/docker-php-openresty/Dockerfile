# Dockerfile - alpine  
# https://github.com/openresty/docker-openresty  
  
FROM alpine:3.6  
  
MAINTAINER tofuiang <tofuliang@gmail.com>  
  
# Docker Build Arguments  
ARG RESTY_VERSION="1.11.2.5"  
ARG RESTY_LUAROCKS_VERSION="2.3.0"  
ARG RESTY_OPENSSL_VERSION="1.0.2k"  
ARG RESTY_PCRE_VERSION="8.40"  
ARG RESTY_CONFIG_OPTIONS="\  
\--with-file-aio \  
\--with-http_addition_module \  
\--with-http_auth_request_module \  
\--with-http_dav_module \  
\--with-http_flv_module \  
\--with-http_geoip_module=dynamic \  
\--with-http_gunzip_module \  
\--with-http_gzip_static_module \  
\--with-http_image_filter_module=dynamic \  
\--with-http_mp4_module \  
\--with-http_random_index_module \  
\--with-http_realip_module \  
\--with-http_secure_link_module \  
\--with-http_slice_module \  
\--with-http_ssl_module \  
\--with-http_stub_status_module \  
\--with-http_sub_module \  
\--with-http_v2_module \  
\--with-http_xslt_module=dynamic \  
\--with-ipv6 \  
\--with-mail \  
\--with-mail_ssl_module \  
\--with-md5-asm \  
\--with-pcre-jit \  
\--with-sha1-asm \  
\--with-stream \  
\--with-stream_ssl_module \  
\--with-threads \  
"  
ARG _RESTY_CONFIG_DEPS="--with-openssl=/tmp/openssl-${RESTY_OPENSSL_VERSION}
\--with-pcre=/tmp/pcre-${RESTY_PCRE_VERSION}"  
  
ARG PHP_INI_DIR="/usr/local/etc"  
# Apply stack smash protection to functions using local buffers and alloca()  
# Make PHP's main executable position-independent (improves ASLR security
mechanism, and has no performance impact on x86_64)  
# Enable optimization (-O2)  
# Enable linker optimization (this sorts the hash buckets to improve cache
locality, and is non-default)  
# Adds GNU HASH segments to generated executables (this is used if present,
and is much faster than sysv hash; in this configuration, sysv hash is also
generated)  
# https://github.com/docker-library/php/issues/272  
ARG PHP_EXTRA_CONFIGURE_ARGS="--enable-fpm --with-fpm-user=www-data --with-
fpm-group=www-data"  
ARG PHP_CFLAGS="-fstack-protector-strong -fpic -fpie -O2"  
ARG PHP_CPPFLAGS="$PHP_CFLAGS"  
ARG PHP_LDFLAGS="-Wl,-O1 -Wl,--hash-style=both -pie"  
  
ARG GPG_KEYS="1729F83938DA44E27BA0F4D3DBDB397470D12172
B1B44D8F021E4E2D6021E995DC9FF8D3EE5AF27F"  
  
ARG PHP_URL="https://secure.php.net/get/php-7.2.4.tar.xz/from/this/mirror"  
ARG
PHP_ASC_URL="https://secure.php.net/get/php-7.2.4.tar.xz.asc/from/this/mirror"  
ARG
PHP_SHA256="7916b1bd148ddfd46d7f8f9a517d4b09cd8a8ad9248734e7c8dd91ef17057a88"  
ARG PHP_MD5=""  
# persistent / runtime deps  
ARG PHPIZE_DEPS="\  
autoconf \  
dpkg-dev dpkg \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkgconf \  
re2c \  
curl-dev \  
libedit-dev \  
libxml2-dev \  
sqlite-dev \  
coreutils \  
libressl-dev \  
libsodium-dev \  
"  
  
ARG PHP_DEPS="\  
ca-certificates \  
curl \  
tar \  
xz \  
# https://github.com/docker-library/php/issues/494  
libressl \  
"  
  
ARG OPENRESTY_BUILD_DEPS="\  
build-base \  
gd-dev \  
geoip-dev \  
libxslt-dev \  
linux-headers \  
make \  
perl-dev \  
readline-dev \  
zlib-dev \  
"  
  
ARG OPENRESTY_DEPS="\  
curl \  
gd \  
geoip \  
libgcc \  
libxslt \  
zlib \  
"  
  
COPY musl-fixes.patch /tmp/musl-fixes.patch  
COPY docker-php-source /usr/local/bin/  
COPY docker-php-ext-* docker-php-entrypoint /usr/local/bin/  
  
# ensure www-data user exists  
RUN set -x \  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data \  
# 82 is the standard uid/gid for "www-data" in Alpine  
# http://git.alpinelinux.org/cgit/aports/tree/main/apache2/apache2.pre-
install?h=v3.3.2  
# http://git.alpinelinux.org/cgit/aports/tree/main/lighttpd/lighttpd.pre-
install?h=v3.3.2  
# http://git.alpinelinux.org/cgit/aports/tree/main/nginx-initscripts/nginx-
initscripts.pre-install?h=v3.3.2  
\  
&& mkdir -p $PHP_INI_DIR/php/conf.d \  
\  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
$OPENRESTY_BUILD_DEPS \  
&& apk add --no-cache --virtual .persistent-deps \  
$PHP_DEPS \  
$OPENRESTY_DEPS \  
\  
&& apk add --no-cache --virtual .fetch-deps \  
gnupg \  
openssl \  
&& apk add --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing \  
gnu-libiconv \  
; \  
\  
#==============PHP-START==============  
mkdir -p /usr/src; \  
cd /usr/src; \  
\  
wget -O php.tar.xz "$PHP_URL"; \  
\  
if [ -n "$PHP_SHA256" ]; then \  
echo "$PHP_SHA256 *php.tar.xz" | sha256sum -c -; \  
fi; \  
if [ -n "$PHP_MD5" ]; then \  
echo "$PHP_MD5 *php.tar.xz" | md5sum -c -; \  
fi; \  
\  
if [ -n "$PHP_ASC_URL" ]; then \  
wget -O php.tar.xz.asc "$PHP_ASC_URL"; \  
export GNUPGHOME="$(mktemp -d)"; \  
for key in $GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done; \  
gpg --batch --verify php.tar.xz.asc php.tar.xz; \  
rm -r "$GNUPGHOME"; \  
fi; \  
\  
apk del .fetch-deps \  
&& export CFLAGS="$PHP_CFLAGS" \  
CPPFLAGS="$PHP_CPPFLAGS" \  
LDFLAGS="$PHP_LDFLAGS" \  
&& docker-php-source extract \  
&& cd /usr/src/php \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/php/conf.d" \  
\  
\--disable-cgi \  
\  
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
\--with-sodium=shared \  
\  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib \  
\  
# bundled pcre does not support JIT on s390x  
#
https://manpages.debian.org/stretch/libpcre3-dev/pcrejit.3.en.html#AVAILABILITY_OF_JIT_SUPPORT  
$(test "$gnuArch" = 's390x-linux-gnu' && echo '--without-pcre-jit') \  
\  
$PHP_EXTRA_CONFIGURE_ARGS \  
&& make -j`grep -c ^processor /proc/cpuinfo` \  
&& make install \  
&& cp /usr/src/php/php.ini-development $PHP_INI_DIR/php.ini-development \  
&& cp /usr/src/php/php.ini-production $PHP_INI_DIR/php.ini-production \  
&& cp /usr/src/php/php.ini-production $PHP_INI_DIR/php.ini \  
&& cp $PHP_INI_DIR/php-fpm.conf.default $PHP_INI_DIR/php-fpm.conf \  
&& cp $PHP_INI_DIR/php-fpm.d/www.conf.default $PHP_INI_DIR/php-fpm.d/www.conf
\  
&& sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' $PHP_INI_DIR/php.ini \  
&& sed -i 's/include=NONE\/etc\/php-
fpm.d\/\\*.conf/include=\/usr\/local\/etc\/php-fpm.d\/*.conf/g'
$PHP_INI_DIR/php-fpm.conf \  
&& sed -i 's/;daemonize = yes/daemonize = no/g' $PHP_INI_DIR/php-fpm.conf \  
&& sed -i 's/user = nobody/user = www-data/g' $PHP_INI_DIR/php-fpm.d/www.conf
\  
&& sed -i 's/group = nobody/group = www-data/g' $PHP_INI_DIR/php-
fpm.d/www.conf \  
&& sed -i 's/;listen.owner = nobody/listen.owner = www-data/g'
$PHP_INI_DIR/php-fpm.d/www.conf \  
&& sed -i 's/;listen.group = www-data/listen.group = www-data/g'
$PHP_INI_DIR/php-fpm.d/www.conf \  
&& sed -i 's/;listen.mode = 0660/listen.mode = 0660/g' $PHP_INI_DIR/php-
fpm.d/www.conf \  
&& sed -i 's/listen = 127.0.0.1:9000/listen = \/var\/run\/php-fpm.sock/g'
$PHP_INI_DIR/php-fpm.d/www.conf \  
&& { find /usr/local/bin /usr/local/sbin -type f -perm +0111 -exec strip
--strip-all '{}' \+ || true; } \  
&& make clean \  
&& docker-php-source delete \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .php-ext-build-deps jpeg-dev libpng-dev
freetype-dev libxml2-dev gettext-dev cyrus-sasl-dev bzip2-dev \  
# 配置GD库,开启更多图片支持  
&& docker-php-ext-configure gd --enable-gd-jis-conv --with-jpeg-dir --with-
png-dir --with-zlib-dir --with-freetype-dir --with-gd \  
# 安装常用扩展  
&& docker-php-ext-install -j`grep -c ^processor /proc/cpuinfo` gd bcmath bz2
calendar dba exif gettext mysqli pdo_mysql shmop soap sockets sysvmsg sysvsem
sysvshm zip \  
# 从源码编译安装支持sasl的libmemcached  
&& curl -fSkL --retry 5
https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz
-o /usr/src/libmemcached-1.0.18.tar.gz \  
&& tar xzf /usr/src/libmemcached-1.0.18.tar.gz -C /usr/src \  
&& mv /tmp/musl-fixes.patch /usr/src/libmemcached-1.0.18/musl-fixes.patch \  
&& cd /usr/src/libmemcached-1.0.18 \  
&& patch -p1 -i musl-fixes.patch \  
&& ./configure --enable-sasl && make -j`grep -c ^processor /proc/cpuinfo` &&
make install \  
# 从源码编译安装支持sasl的memcached扩展  
&& curl -fSkL --retry 5 http://pecl.php.net/get/memcached-3.0.4.tgz -o
/usr/src/memcached-3.0.4.tgz \  
&& tar xzf /usr/src/memcached-3.0.4.tgz -C /usr/src \  
&& cd /usr/src/memcached-3.0.4 \  
&& phpize && ./configure --enable-memcached --enable-memcached-json --enable-
shared --disable-static && make -j`grep -c ^processor /proc/cpuinfo` && make
install \  
&& docker-php-ext-enable memcached \  
# 从源码编译安装 tideways 扩展  
&& curl -fSkL --retry 5 https://codeload.github.com/tideways/php-profiler-
extension/tar.gz/v4.1.5 -o /usr/src/tideways-4.1.5.tar.gz \  
&& tar xzf /usr/src/tideways-4.1.5.tar.gz -C /usr/src \  
&& cd /usr/src/php-xhprof-extension-4.1.5 \  
&& phpize && ./configure --enable-shared --disable-static && make -j`grep -c
^processor /proc/cpuinfo` && make install \  
&& docker-php-ext-enable tideways \  
# 使用pecl安装redis扩展  
&& pecl install redis yac-2.0.2 yaf-3.0.7 swoole-2.1.1 xdebug \  
&& docker-php-ext-enable redis yac yaf swoole sodium \  
# strip 所有扩展  
&& rm -fr /usr/local/lib/php/extensions/no-debug-non-zts-20170718/opcache.a \  
&& rm -fr /usr/local/lib/php/extensions/no-debug-non-zts-20170718/sodium.a \  
&& echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20170718/opcache.so' > /usr/local/etc/php/conf.d/docker-php-ext-
opcache.ini \  
&& strip /usr/local/lib/php/extensions/no-debug-non-zts-20170718/* \  
# 删除源码文件  
&& { mkdir /opt || true; } && cd /opt && curl -fSkL --retry 5
https://codeload.github.com/Mirocow/pydbgpproxy/zip/master -o master.zip \  
&& unzip master.zip && rm -fr master.zip && mv pydbgpproxy-master
PHPRemoteDBGp \  
&& phpExtrunDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
#==============PHP-END==============  
\  
#==============OPENRESTY-START==============  
\  
# These are not intended to be user-specified  
# 1) Install apk dependencies  
# 2) Download and untar OpenSSL, PCRE, and OpenResty  
# 3) Build OpenResty  
# 4) Cleanup  
&& export CFLAGS="" \  
CPPFLAGS="" \  
LDFLAGS="" \  
&& cd /tmp \  
&& curl -fSkL --retry 5
https://www.openssl.org/source/openssl-${RESTY_OPENSSL_VERSION}.tar.gz -o
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& tar xzf openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
&& curl -fSkL --retry 5
https://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-${RESTY_PCRE_VERSION}.tar.gz
-o pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& tar xzf pcre-${RESTY_PCRE_VERSION}.tar.gz \  
&& curl -fSkL --retry 5
https://openresty.org/download/openresty-${RESTY_VERSION}.tar.gz -o
openresty-${RESTY_VERSION}.tar.gz \  
&& tar xzf openresty-${RESTY_VERSION}.tar.gz \  
&& cd /tmp/openresty-${RESTY_VERSION} \  
&& ./configure -j`grep -c ^processor /proc/cpuinfo` ${_RESTY_CONFIG_DEPS}
${RESTY_CONFIG_OPTIONS} \  
&& make -j`grep -c ^processor /proc/cpuinfo` \  
&& make -j`grep -c ^processor /proc/cpuinfo` install \  
&& cd /tmp \  
&& rm -rf \  
openssl-${RESTY_OPENSSL_VERSION} \  
openssl-${RESTY_OPENSSL_VERSION}.tar.gz \  
openresty-${RESTY_VERSION}.tar.gz openresty-${RESTY_VERSION} \  
pcre-${RESTY_PCRE_VERSION}.tar.gz pcre-${RESTY_PCRE_VERSION} \  
&& { find /usr/local/openresty -type f -perm +0111 -exec strip --strip-all
'{}' \+ || true; } \  
\  
#==============OPENRESTY-END==============  
\  
&& apk del .build-deps \  
&& apk del .php-ext-build-deps \  
&& apk add --no-cache --virtual .php-rundeps $runDeps \  
&& apk add --no-cache --virtual .php-ext-rundeps $phpExtrunDeps \  
&& rm -fr /usr/src/* \  
&& apk add --no-cache supervisor openssh \  
# 日志目录  
&& mkdir -p /usr/local/var/log/php-fpm/ \  
&& mkdir -p /usr/local/var/log/php_errors/ \  
&& mkdir -p /usr/local/var/log/php_slow/ \  
&& mkdir -p /usr/local/var/log/nginx/ \  
&& chown www-data:www-data -R /usr/local/var/log \  
# SSH  
&& { mkdir /var/run/sshd || true; } \  
&& ssh-keygen -t rsa -b 4096 -f /etc/ssh/ssh_host_rsa_key -P "" \  
&& echo "PermitRootLogin yes" >> /etc/ssh/sshd_config  
  
# Add additional binaries into PATH for convenience  
ENV
PATH=$PATH:/usr/local/openresty/luajit/bin/:/usr/local/openresty/nginx/sbin/:/usr/local/openresty/bin/  
ENV PYTHONPATH=$PYTHONPATH:/opt/bin/PHPRemoteDBGp/pythonlib  
ENV LD_PRELOAD=/usr/lib/preloadable_libiconv.so  
  
ADD etc/supervisor /etc/supervisor  
ADD etc/php/conf.d /usr/local/etc/php/conf.d/  
ADD etc/php/php-fpm.d /usr/local/etc/php-fpm.d/  
ADD daemon /usr/local/bin/daemon  
  
# Expose ports  
# SSH  
EXPOSE 22  
# NGINX  
EXPOSE 80  
EXPOSE 443  
# Xdebug  
EXPOSE 9001  
  
CMD ["/usr/local/bin/daemon"]  
  

