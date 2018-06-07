###  
# LaVue  
#  
# Repository: LaVue  
# Image: PHP  
# Version: 7.2.x  
# Strategy: PHP-FPM From Base Alpine Image Forked from Official PHP-FPM-Alpine  
# Base distro: Alpine 3.7  
#  
  
FROM lavue/alpine  
  
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
ENV \  
VERSION=0.4.5 \  
PHP_VERSION="7.2.4" \  
ALPINE_VERSION="3.7" \  
# http://www.php.net/downloads.php  
PHP_SHA256="7916b1bd148ddfd46d7f8f9a517d4b09cd8a8ad9248734e7c8dd91ef17057a88"  
# Separate ENV for substitute PHP_VERSION in PHP_URL && PHP_ASC_URL  
ENV \  
# http://fi2.php.net/downloads.php#gpg-7.2  
GPG_KEYS=" \  
1729F83938DA44E27BA0F4D3DBDB397470D12172 \  
B1B44D8F021E4E2D6021E995DC9FF8D3EE5AF27F \  
" \  
PHP_CFLAGS="-fstack-protector-strong -fpic -fpie -O2" \  
PHP_CPPFLAGS="-fstack-protector-strong -fpic -fpie -O2" \  
PHP_LDFLAGS="-Wl,-O1 -Wl,--hash-style=both -pie" \  
PHP_URL="https://secure.php.net/get/php-$PHP_VERSION.tar.xz/from/this/mirror"
\  
PHP_ASC_URL="https://secure.php.net/get/php-$PHP_VERSION.tar.xz.asc/from/this/mirror"
\  
PHP_MD5="" \  
PHP_EXTRA_CONFIGURE_ARGS=" \  
\--enable-fpm \  
\--with-fpm-user=www-data \  
\--with-fpm-group=www-data \  
" \  
PHP_INI_DIR="/usr/local/etc/php" \  
# persistent / runtime deps  
PHPIZE_DEPS=" \  
autoconf \  
dpkg-dev dpkg \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkgconf \  
re2c \  
"  
  
LABEL name = "PHP"  
LABEL description = "PHP-FPM for LaVue"  
LABEL maintainer = "4mydom@gmail.com"  
LABEL version = "$VERSION-$PHP_VERSION-$ALPINE_VERSION"  
  
COPY scripts/ /usr/local/bin/  
  
RUN \  
set -xe \  
&& apk add --no-cache --virtual .persistent-deps \  
# already installed in lavue/alpine  
# ca-certificates \  
# curl \  
# tar \  
xz \  
# https://github.com/docker-library/php/issues/494  
libressl \  
&& apk add --no-cache --virtual .fetch-deps \  
gnupg \  
&& mkdir -p $PHP_INI_DIR/conf.d \  
&& mkdir -p /usr/src \  
&& cd /usr/src \  
&& wget -O php.tar.xz "$PHP_URL" \  
&& \  
if [ -n "$PHP_SHA256" ]; then \  
echo "$PHP_SHA256 *php.tar.xz" | sha256sum -c -; \  
fi; \  
\  
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
rm -rf "$GNUPGHOME"; \  
fi; \  
\  
apk del .fetch-deps \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
coreutils \  
curl-dev \  
libedit-dev \  
libressl-dev \  
libsodium-dev \  
libxml2-dev \  
sqlite-dev \  
\  
&& export CFLAGS="$PHP_CFLAGS" \  
CPPFLAGS="$PHP_CPPFLAGS" \  
LDFLAGS="$PHP_LDFLAGS" \  
\  
&& docker-php-source extract \  
&& cd /usr/src/php \  
&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
&& ./configure \  
\--build="$gnuArch" \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
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
\--with-sodium \  
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
&& make -j "$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -perm +0111 -exec strip
--strip-all '{}' \+ || true; } \  
&& make clean \  
&& cd / \  
\  
# https://github.com/docker-library/php/issues/443  
&& pecl update-channels \  
\  
&& apk add --no-cache --virtual .ext-deps \  
bzip2-dev \  
freetype-dev \  
icu-dev \  
imap-dev\  
libjpeg-turbo-dev \  
libpng-dev \  
libwebp-dev \  
libxml2-dev \  
libxpm-dev \  
\  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-webp-dir=/usr/include/ \  
\--with-xpm-dir=/usr/include/ \  
&& docker-php-ext-configure imap \  
\--with-imap \  
\--with-imap-ssl \  
&& docker-php-ext-install \  
bcmath \  
bz2 \  
calendar \  
exif \  
gd \  
intl \  
imap \  
mysqli \  
opcache \  
pcntl \  
pdo \  
pdo_mysql \  
posix \  
soap \  
xml \  
zip \  
\  
&& pecl install xdebug \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --no-cache --virtual .php-rundeps $runDeps \  
\  
&& docker-php-source delete \  
&& apk del .build-deps \  
&& apk del .ext-deps \  
&& rm -rf ~/.pearrc \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
COPY conf/ /usr/local/etc/  
  
ENTRYPOINT ["docker-php-entrypoint"]  
  
WORKDIR /var/www/html  
  
EXPOSE 9000  
  
CMD ["php-fpm"]  

