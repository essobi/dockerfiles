FROM alpine:3.7  
# Build ARGS  
ARG VCS_REF  
ARG BUILD_DATE  
ARG PHP_VERSION="7.2.3"  
ARG
PHP_SHA256="b3a94f1b562f413c0b96f54bc309706d83b29ac65d9b172bc7ed9fb40a5e651f"  
# Labels and meta-data  
LABEL maintainer="James Brink, brink.james@gmail.com" \  
decription="PHP ${PHP_VERSION}} with Apache" \  
version="${PHP_VERSION}" \  
org.label-schema.name="php" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jamesbrink/docker-php" \  
org.label-schema.schema-version="1.0.0-rc1"  
# Copy in our assets.  
COPY docker-assets/ /  
  
# Set our ENV variables.  
ENV PHP_CFLAGS="-fstack-protector-strong -fpic -fpie -O2" \  
PHP_CPPFLAGS="$PHP_CFLAGS" \  
PHP_LDFLAGS="-Wl,-O1 -Wl,--hash-style=both -pie" \  
GPG_KEYS="1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763 \  
6E4F6AB321FDC07F2C332E3AC2BF0BC433CFC8B3 \  
A917B1ECDA84AEC2B568FED6F50ABC807BD5DCD0 \  
528995BFEDFBA7191D46839EF9BA0ADA31CBD89E \  
1729F83938DA44E27BA0F4D3DBDB397470D12172 \  
B1B44D8F021E4E2D6021E995DC9FF8D3EE5AF27F" \  
PHP_VERSION="${PHP_VERSION}" \  
PHP_URL="https://secure.php.net/get/php-${PHP_VERSION}.tar.xz/from/this/mirror"
\  
PHP_ASC_URL="https://secure.php.net/get/php-${PHP_VERSION}.tar.xz.asc/from/this/mirror"
\  
PHP_SHA256="${PHP_SHA256}" \  
PHP_INI_DIR="/usr/local/etc/php" \  
APACHE_LOG_LEVEL="warn"  
# persistent / runtime deps  
RUN set -xe; \  
apk add --no-cache --virtual .persistent-deps \  
apache2 \  
ca-certificates \  
curl \  
libpcre16 \  
libpcre32 \  
libpcrecpp \  
libressl \  
tar \  
xz; \  
mkdir -p $PHP_INI_DIR/conf.d; \  
apk add --no-cache --virtual .fetch-deps gnupg; \  
mkdir -p /usr/src; \  
cd /usr/src; \  
wget -O php.tar.xz "$PHP_URL"; \  
if [ -n "$PHP_SHA256" ]; then echo "$PHP_SHA256 *php.tar.xz" | sha256sum -c -;
fi; \  
if [ -n "$PHP_MD5" ]; then echo "$PHP_MD5 *php.tar.xz" | md5sum -c -; fi; \  
if [ -n "$PHP_ASC_URL" ]; then \  
wget -O php.tar.xz.asc "$PHP_ASC_URL"; \  
export GNUPGHOME="$(mktemp -d)"; \  
for key in $GPG_KEYS; do \  
gpg --keyserver ipv4.pool.sks-keyservers.net --recv-keys "$key"; \  
done; \  
gpg --batch --verify php.tar.xz.asc php.tar.xz; \  
rm -rf "$GNUPGHOME"; \  
fi; \  
apk del .fetch-deps; \  
apk add --no-cache --virtual .build-deps \  
apache2-dev \  
autoconf \  
coreutils \  
curl-dev \  
dpkg-dev dpkg \  
file \  
g++ \  
gcc \  
libc-dev \  
libedit-dev \  
libressl-dev \  
libxml2-dev \  
make \  
pcre-dev \  
pkgconf \  
re2c \  
sqlite-dev; \  
export CFLAGS="$PHP_CFLAGS" \  
CPPFLAGS="$PHP_CPPFLAGS" \  
LDFLAGS="$PHP_LDFLAGS"; \  
docker-php-source extract; \  
cd /usr/src/php; \  
gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \  
./configure \  
\--build="$gnuArch" \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
\--with-apxs2=/usr/bin/apxs \  
\--disable-cgi \  
\--enable-ftp \  
\--enable-mbstring \  
\--enable-mysqlnd \  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib \  
\--with-pcre-regex=/usr \  
$(test "$gnuArch" = 's390x-linux-gnu' && echo '--without-pcre-jit') \  
$PHP_EXTRA_CONFIGURE_ARGS; \  
make -j "$(nproc)"; \  
make install; \  
{ find /usr/local/bin /usr/local/sbin -type f -perm +0111 -exec strip --strip-
all '{}' \+ || true; }; \  
make clean; \  
cd /; \  
docker-php-source delete; \  
runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' --recursive /usr/local \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)"; \  
apk add --no-cache --virtual .php-rundeps $runDeps; \  
apk del .build-deps; \  
pecl update-channels; \  
rm -rf /tmp/pear ~/.pearrc; \  
mkdir /run/apache2; \  
rm /var/www/localhost/htdocs/index.html  
  
ENTRYPOINT ["docker-php-entrypoint"]  
  
CMD ["/usr/local/bin/apache2-foreground"]

