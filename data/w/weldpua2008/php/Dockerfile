FROM debian:wheezy  
# based on https://raw.githubusercontent.com/docker-
library/php/4677ca134fe48d20c820a19becb99198824d78e3/5.5/Dockerfile  
  
MAINTAINER Valeriy Solovyov <weldpua2008@gmail.com>  
  
WORKDIR /var/www/html  
COPY docker-php-ext-* /usr/local/bin/  
  
VOLUME /var/www/html  
# yes '' | pecl install -f apc  
RUN export DEBIAN_FRONTEND=noninteractive && \  
export DEBIAN_RELEASE=$(awk -F'[" ]' '/VERSION=/{print $3}' /etc/os-release |
tr -cd '[[:alnum:]]._-' ) && \  
[[ "x${DEBIAN_RELEASE}" = "x" ]] && export DEBIAN_RELEASE="unstable" || echo
"it's ok" && \  
echo "deb http://httpredir.debian.org/debian ${DEBIAN_RELEASE} main contrib
non-free " > /etc/apt/sources.list && \  
echo "deb http://httpredir.debian.org/debian ${DEBIAN_RELEASE}-updates main
contrib non-free " >> /etc/apt/sources.list && \  
echo "deb http://security.debian.org ${DEBIAN_RELEASE}/updates main contrib
non-free" >> /etc/apt/sources.list && \  
echo "deb-src http://httpredir.debian.org/debian ${DEBIAN_RELEASE} main
contrib non-free" >> /etc/apt/sources.list && \  
echo "deb-src http://httpredir.debian.org/debian ${DEBIAN_RELEASE}-updates
main contrib non-free" >> /etc/apt/sources.list && \  
echo "deb-src http://security.debian.org ${DEBIAN_RELEASE}/updates main
contrib non-free" >> /etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y apt-utils autoconf file g++ gcc libc6-dev make pkg-config
re2c --no-install-recommends && \  
apt-get install -y ca-certificates curl libedit2 libsqlite3-0 libxml2 --no-
install-recommends && \  
export PHP_INI_DIR=/usr/local/etc/php && \  
mkdir -p $PHP_INI_DIR/conf.d && \  
export PHP_EXTRA_CONFIGURE_ARGS=" --enable-fpm --with-fpm-user=www-data
--with-fpm-group=www-data" && \  
export GPG_KEYS="0B96609E270F565C13292B24C13C70B87267B52D
0BD78B5F97500D450838F95DFE857D9A90D90EC1
F38252826ACD957EF380D39F2F7956BC5DA04B5D" && \  
export PHP_VERSION=5.3.27 && \  
export PHP_FILENAME=php-5.3.27.tar.bz2 && \  
export PHP_MD5=25ae23a5b9615fe8d33de5b63e1bb788 && \  
set -xe && \  
export buildDeps="$PHP_EXTRA_BUILD_DEPS libcurl4-openssl-dev libedit-dev
libsqlite3-dev libssl-dev libxml2-dev xz-utils bzip2" && \  
apt-get install -y $buildDeps \--no-install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
curl -fSL "http://php.net/get/$PHP_FILENAME/from/this/mirror" -o
"$PHP_FILENAME" && \  
echo "$PHP_MD5 *$PHP_FILENAME" | md5sum -c - && \  
curl -fSL "http://php.net/get/$PHP_FILENAME.asc/from/this/mirror" -o
"$PHP_FILENAME.asc" && \  
export GNUPGHOME="$(mktemp -d)" && \  
for key in $GPG_KEYS; do gpg --keyserver hkp://ha.pool.sks-keyservers.net:80
--recv-keys "$key"; done && \  
gpg --batch --verify "$PHP_FILENAME.asc" "$PHP_FILENAME" && \  
rm -r "$GNUPGHOME" "$PHP_FILENAME.asc" && \  
mkdir -p /usr/src/php && \  
tar jxf "$PHP_FILENAME" -C /usr/src/php --strip-components=1 && \  
rm "$PHP_FILENAME" && \  
cd /usr/src/php && \  
./configure --with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
\--disable-cgi \  
\--enable-mysqlnd \  
\--enable-mbstring \  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-zlib $PHP_EXTRA_CONFIGURE_ARGS && \  
make -j"$(nproc)" && \  
make install && \  
{ find /usr/local/bin /usr/local/sbin -type f -executable -exec strip --strip-
all '{}' \+ || true; } && \  
make clean && \  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false
-o APT::AutoRemove::SuggestsImportant=false $buildDeps && \  
rm -r /var/lib/apt/lists/* && \  
set -ex \  
&& cd /usr/local/etc \  
&& if [ -d php-fpm.d ]; then \  
# for some reason, upstream's php-fpm.conf.default has "include=NONE/etc/php-
fpm.d/*.conf"  
sed 's!=NONE/!=!g' php-fpm.conf.default | tee php-fpm.conf > /dev/null; \  
cp php-fpm.d/www.conf.default php-fpm.d/www.conf; \  
else \  
# PHP 5.x don't use "include=" by default, so we'll create our own simple
config that mimics PHP 7+ for consistency  
mkdir php-fpm.d; \  
cp php-fpm.conf.default php-fpm.d/www.conf; \  
{ \  
echo '[global]'; \  
echo 'include=etc/php-fpm.d/*.conf'; \  
} | tee php-fpm.conf; \  
fi \  
&& { \  
echo '[global]'; \  
echo 'error_log = /proc/self/fd/2'; \  
echo; \  
echo '[www]'; \  
echo '; if we send this to /proc/self/fd/1, it never appears'; \  
echo 'access.log = /proc/self/fd/2'; \  
echo; \  
echo '; clear_env = no'; \  
echo; \  
echo '; Ensure worker stdout and stderr are sent to the main error log.'; \  
echo 'catch_workers_output = yes'; \  
} | tee php-fpm.d/docker.conf \  
&& { \  
echo '[global]'; \  
echo 'daemonize = no'; \  
echo; \  
echo '[www]'; \  
echo 'listen = [::]:9000'; \  
} | tee php-fpm.d/zz-docker.conf \  
&& set +e && \  
apt-get update && \  
apt-get install -y libpng12-dev libjpeg-dev libmysqlclient-dev libmcrypt-dev
&& \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr && \  
docker-php-ext-install gd mysqli mbstring mcrypt zip pdo_mysql && \  
pecl install -o -f zendopcache && \  
{ \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini && \  
export WORDPRESS_VERSION=4.5.2 && \  
export WORDPRESS_SHA1=bab94003a5d2285f6ae76407e7b1bbb75382c36e && \  
curl -o wordpress.tar.gz -SL
https://wordpress.org/wordpress-${WORDPRESS_VERSION}.tar.gz && \  
echo "$WORDPRESS_SHA1 *wordpress.tar.gz" | sha1sum -c - && \  
tar -xzf wordpress.tar.gz -C /usr/src/ && \  
rm wordpress.tar.gz && \  
chown -R www-data:www-data /usr/src/wordpress  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["php-fpm"]  

