FROM alpine:latest  
  
MAINTAINER YoungMan "bushengquan@eastspider.com"  
  
LABEL description="walle-web集成Nginx,MariaDB,PHP版"  
  
ENV PHPIZE_DEPS \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkgconf \  
re2c  
RUN set -xe \  
&&apk add --no-cache --virtual .persistent-deps \  
ca-certificates \  
openssl \  
curl \  
tar \  
xz \  
git \  
nginx \  
mariadb \  
mariadb-client \  
unzip \  
subversion \  
ansible \  
openssh-client  
  
ENV PHP_INI_DIR /etc/php  
RUN mkdir -p $PHP_INI_DIR/conf.d && \  
mkdir -p /etc/ansible && \  
touch /etc/ansible/hosts && \  
wget -q -O /etc/ansible/ansible.cfg
https://raw.githubusercontent.com/ansible/ansible/devel/examples/ansible.cfg  
  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=nginx --with-fpm-
group=nginx  
  
ENV GPG_KEYS 0BD78B5F97500D450838F95DFE857D9A90D90EC1
6E4F6AB321FDC07F2C332E3AC2BF0BC433CFC8B3  
  
ENV PHP_VERSION 5.6.26  
ENV PHP_FILENAME php-5.6.26.tar.xz  
ENV PHP_SHA256
203a854f0f243cb2810d1c832bc871ff133eccdf1ff69d32846f93bc1bef58a8  
  
ENV REDIS_VERSION 2.2.8  
ENV REDIS_FILENAME redis-2.2.8.tgz  
  
COPY docker-php-source /usr/local/bin/  
  
RUN set -xe \  
&& apk add --no-cache --virtual .fetch-deps \  
gnupg \  
&& mkdir -p /usr/src \  
&& cd /usr/src \  
&& curl -fSL "https://secure.php.net/get/$PHP_FILENAME/from/this/mirror" -o
php.tar.xz \  
&& apk add --no-cache --virtual .build-deps \  
$PHPIZE_DEPS \  
curl-dev \  
libedit-dev \  
libxml2-dev \  
libssh2-dev \  
libressl-dev \  
sqlite-dev \  
gettext \  
libmcrypt-dev \  
icu-libs \  
zlib-dev \  
libpng-dev \  
intltool \  
gettext-dev \  
icu \  
icu-dev \  
libvpx-dev \  
libjpeg-turbo-dev \  
freetype-dev \  
imap-dev \  
bzip2-dev \  
&& docker-php-source extract \  
&& cd /usr/src/php \  
&& wget http://pecl.php.net/get/$REDIS_FILENAME -O /usr/src/php/ext/redis.tgz
\  
&& tar xf /usr/src/php/ext/redis.tgz -C /usr/src/php/ext \  
&& mv /usr/src/php/ext/redis-${REDIS_VERSION} /usr/src/php/ext/redis \  
&& ./configure \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
\  
\--disable-cgi \  
\--disable-ipv6 \  
\  
\--enable-ftp \  
\--enable-mbstring \  
\--enable-mysqlnd \  
\--enable-sockets \  
\--enable-sysvsem \  
\--enable-sysvshm \  
\--enable-opcache \  
\--enable-exif \  
\--enable-zip \  
\--enable-intl \  
\--enable-mbregex \  
\  
\--with-pcre-regex \  
\--with-curl \  
\--with-libedit \  
\--with-openssl \  
\--with-mysql \  
\--with-zlib \  
\--with-mcrypt \  
\--with-gettext \  
\--with-readline \  
\--with-gd \  
\--with-mhash \  
\--with-iconv-dir \  
\--with-pcre-dir \  
\--with-jpeg-dir \  
\--with-png-dir \  
\--with-vpx-dir \  
\--with-freetype-dir \  
\--with-imap \  
\--with-litespeed \  
\--with-bz2 \  
\  
$PHP_EXTRA_CONFIGURE_ARGS \  
&& make -j"$(getconf _NPROCESSORS_ONLN)" \  
&& make install \  
&& cp php.ini-production $PHP_INI_DIR/php.ini \  
&& cd /usr/src/php/ext/redis \  
&& phpize \  
&& ./configure --with-php-config=/usr/local/bin/php-config \  
&& make \  
&& make install \  
&& echo 'extension="redis.so"' >> $PHP_INI_DIR/php.ini \  
&& cd /usr/src/php \  
&& { find /usr/local/bin /usr/local/sbin -type f -perm +0111 -exec strip
--strip-all '{}' + || true; } \  
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
&& apk add --no-cache --virtual .php-rundeps $runDeps  
  
RUN set -ex \  
&& cd /etc \  
&& if [ -d php-fpm.d ]; then \  
# for some reason, upstream's php-fpm.conf.default has "include=NONE/etc/php-
fpm.d/*.conf"  
sed 's!=NONE/!=!g' php-fpm.conf.default | tee php-fpm.conf > /dev/null; \  
cp php-fpm.d/www.conf.default php-fpm.d/www.conf; \  
else \  
mkdir php-fpm.d; \  
cp php-fpm.conf.default php-fpm.d/www.conf; \  
{ \  
echo '[global]'; \  
echo 'include=/etc/php-fpm.d/*.conf'; \  
} | tee php-fpm.conf; \  
fi \  
&& { \  
echo '[global]'; \  
echo 'error_log = /proc/self/fd/2'; \  
echo 'daemonize = no'; \  
echo; \  
echo '[www]'; \  
echo 'access.log = /proc/self/fd/2'; \  
echo 'clear_env = no'; \  
echo 'catch_workers_output = yes'; \  
echo 'user = nginx'; \  
echo 'group = nginx'; \  
echo 'listen.backlog = 4096'; \  
echo 'listen.owner = nginx'; \  
echo 'listen.group = nginx'; \  
echo 'listen.mode = 0660'; \  
echo 'listen = [::]:9000'; \  
echo ';listen = /var/run/php-fpm.sock'; \  
echo 'rlimit_files = 65536'; \  
echo 'pm = dynamic'; \  
echo 'pm.max_children = 150'; \  
echo 'pm.start_servers = 10'; \  
echo 'pm.min_spare_servers = 10'; \  
echo 'pm.max_spare_servers = 100'; \  
echo 'request_terminate_timeout = 10m'; \  
} | tee php-fpm.d/socket.conf \  
&& ln -s /etc/php-fpm.conf /usr/local/etc/php-fpm.conf  
  
COPY docker-php-ext-* /usr/local/bin/  
  
RUN docker-php-ext-install bcmath intl mbstring mcrypt mysqli opcache
pdo_mysql  
  
ADD ./walle.ini /etc/php/conf.d/walle.ini  
ADD ./entrypoint.sh /entrypoint.sh  
ADD ./nginx.conf /etc/nginx/nginx.conf  
  
WORKDIR /opt/walle-web  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer  
RUN git clone https://github.com/meolu/walle-web /opt/walle-web \  
&&composer install --prefer-dist --no-dev --optimize-autoloader -vvvv \  
&& chmod +x /entrypoint.sh \  
&& chown -R nginx:nginx /opt/walle-web \  
&& mkdir -p /opt/mysql/walle \  
&& chown -R mysql:mysql /opt/mysql/walle \  
&& apk del .build-deps \  
&& apk del .fetch-deps \  
&& rm -rf /usr/src/php*  
  
ENV SERVER_NAME="walle.company.com" DATADIR="/opt/mysql"  
  
EXPOSE 80 3306 9000  
  
VOLUME ["/opt/walle-web", "/opt/mysql"]  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["php-fpm"]  

