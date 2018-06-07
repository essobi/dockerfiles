FROM datenarong/docker-debian-apache:2.4  
MAINTAINER Yamada Yoseigi (datenarong@gmail.com)  
  
# Persistent / runtime deps  
ENV PHPIZE_DEPS \  
autoconf \  
file \  
gcc \  
libc-dev \  
pkg-config \  
re2c  
  
RUN apt-get update && \  
apt-get install -yq --allow-downgrades --no-install-recommends \  
$PHPIZE_DEPS \  
unzip  
  
ENV PHP_EXTRA_BUILD_DEPS apache2-dev  
ENV PHP_EXTRA_CONFIGURE_ARGS --with-apxs2  
  
# Make directory for phpini  
ENV PHP_INI_DIR /usr/local/etc/php  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
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
ENV PHP_CFLAGS="-fstack-protector-strong -fpic -fpie -O2"  
ENV PHP_CPPFLAGS="$PHP_CFLAGS"  
ENV PHP_LDFLAGS="-Wl,-O1 -Wl,--hash-style=both -pie"  
ENV GPG_KEYS A917B1ECDA84AEC2B568FED6F50ABC807BD5DCD0
528995BFEDFBA7191D46839EF9BA0ADA31CBD89E  
  
ENV PHP_VERSION 7.1.8  
ENV
PHP_URL="https://secure.php.net/get/php-$PHP_VERSION.tar.xz/from/this/mirror"
PHP_ASC_URL="https://secure.php.net/get/php-$PHP_VERSION.tar.xz.asc/from/this/mirror"  
ENV
PHP_SHA256="8943858738604acb33ecedb865d6c4051eeffe4e2d06f3a3c8f794daccaa2aab"
PHP_MD5=""  
# Install PHP  
RUN set -xe; \  
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
rm -rf "$GNUPGHOME"; \  
fi;  
  
COPY docker-php-source /usr/local/bin/  
  
ENV buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
freetds-dev \  
libcurl4-openssl-dev \  
libaio-dev \  
libedit-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libpcre3-dev \  
libpng-dev \  
libsqlite3-dev \  
libssh2-1-dev \  
libssl-dev \  
libxml2-dev \  
openssl \  
unixodbc-dev \  
zlib1g-dev \  
"  
RUN set -xe && \  
apt-get update && \  
apt-get install -y --no-install-recommends $buildDeps && \  
\  
export CFLAGS="$PHP_CFLAGS" \  
CPPFLAGS="$PHP_CPPFLAGS" \  
LDFLAGS="$PHP_LDFLAGS" && \  
docker-php-source extract && \  
cd /usr/src/php && \  
gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" && \  
debMultiarch="$(dpkg-architecture --query DEB_BUILD_MULTIARCH)" && \  
# https://bugs.php.net/bug.php?id=74125  
if [ ! -d /usr/include/curl ]; then \  
ln -sT "/usr/include/$debMultiarch/curl" /usr/local/include/curl; \  
fi && \  
./configure \  
\--build="$gnuArch" \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
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
\  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib \  
\  
# bundled pcre is too old for s390x (which isn't exactly a good sign)  
# /usr/src/php/ext/pcre/pcrelib/pcre_jit_compile.c:65:2: error: #error
Unsupported architecture  
\--with-pcre-regex=/usr \  
\--with-libdir="lib/$debMultiarch" \  
\  
$PHP_EXTRA_CONFIGURE_ARGS && \  
make -j "$(nproc)" && \  
make install && \  
{ find /usr/local/bin /usr/local/sbin -type f -executable -exec strip --strip-
all '{}' \+ || true; } && \  
make clean && \  
cd / && \  
docker-php-source delete \  
\  
# https://github.com/docker-library/php/issues/443  
&& pecl update-channels \  
&& rm -rf /tmp/pear ~/.pearrc  
  
COPY docker-php-ext-* /usr/local/bin/  
  
##########################  
# Install PHP extensions #  
##########################  
# APCu and APC backward compatibility  
RUN pecl install apcu && \  
pecl install apcu_bc-1.0.3 && \  
docker-php-ext-enable apcu --ini-name 10-docker-php-ext-apcu.ini && \  
docker-php-ext-enable apc --ini-name 20-docker-php-ext-apc.ini  
  
# ftp  
RUN docker-php-ext-install ftp  
  
# iconv  
RUN docker-php-ext-install iconv  
  
# intl  
RUN docker-php-ext-install intl  
  
# mbstring  
RUN docker-php-ext-install mbstring  
  
# mcrypt  
RUN apt-get update && \  
apt-get install -y libmcrypt-dev && \  
apt-get update && \  
docker-php-ext-install mcrypt  
  
# mongodb  
RUN pecl install mongodb && \  
docker-php-ext-enable mongodb  
  
# mysqli  
RUN docker-php-ext-install mysqli  
  
# opcache  
RUN docker-php-ext-enable opcache  
  
# phalcon (Phalcon Framework 3)  
RUN apt-get update && \  
mkdir /home/phalcon && \  
cd /home/phalcon && \  
git clone \--depth=1 http://github.com/phalcon/cphalcon.git && \  
cd cphalcon/build && \  
./install && \  
echo 'extension=phalcon.so' > $PHP_INI_DIR/conf.d/phalcon.ini  
  
# pcntl  
RUN docker-php-ext-install pcntl  
  
# pdo_mysql  
RUN docker-php-ext-install pdo_mysql  
  
# redis  
RUN pecl install redis && \  
docker-php-ext-enable redis  
  
# soap  
RUN docker-php-ext-install soap  
  
# sockets  
RUN docker-php-ext-install sockets  
  
# ssh2  
RUN pecl install ssh2-1 channel://pecl.php.net/ssh2-1.0 && \  
docker-php-ext-enable ssh2  
  
# xdebug  
RUN pecl install xdebug-beta && \  
docker-php-ext-enable xdebug  
  
# zip  
RUN docker-php-ext-install zip  
  
# Install PHPUnit  
RUN wget https://phar.phpunit.de/phpunit.phar -O /usr/local/bin/phpunit && \  
chmod +x /usr/local/bin/phpunit  
  
# Install composer  
ENV COMPOSER_VERSION 1.4.2  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer --version=${COMPOSER_VERSION} && \  
composer self-update  
  
# Clean cash  
RUN apt-get -y clean && \  
rm -r /var/lib/apt/lists/* && \  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
$buildDeps  
  
# Enable Apache2 modules  
RUN a2enmod rewrite vhost_alias headers ssl  
  
WORKDIR /var/www/html

