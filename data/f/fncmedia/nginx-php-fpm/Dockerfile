FROM ubuntu:15.04  
  
MAINTAINER carsten.eilers@twt.de  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV APPLICATION_NAME web-application  
  
  
  
ENV NGINX_VERSION 1.8.1-1~vivid  
ENV NGINX_GPG_KEY 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62  
  
  
ENV PHP_VERSION 7.0.12  
ENV PHP_URL="https://secure.php.net/get/php-7.0.12.tar.xz/from/this/mirror"  
ENV
PHP_ASC_URL="https://secure.php.net/get/php-7.0.12.tar.xz.asc/from/this/mirror"  
ENV
PHP_SHA256="f3d6c49e1c242e5995dec15e503fde996c327eb86cd7ec45c690e93c971b83ff"  
ENV PHP_MD5="bdcc4dbdac90c2a39422786653059f70"  
ENV PHP_GPG_KEYS 1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763  
  
ENV PHP_INI_DIR /usr/local/etc/php  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=www-data --with-fpm-
group=www-data  
  
  
######## BASE ENV ###########  
# Allow Running with User www-data  
RUN usermod -u 1000 www-data  
RUN chsh -s /bin/bash www-data  
  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkg-config \  
re2c \  
ca-certificates \  
curl \  
wget \  
xz-utils \  
locales \  
libedit2 \  
libsqlite3-0 \  
libxml2 \  
libcurl4-openssl-dev \  
libedit-dev \  
libsqlite3-dev \  
libxml2-dev \  
libicu-dev \  
libpng-dev \  
libjpeg-dev \  
libfreetype6-dev \  
libmcrypt-dev \  
libpq-dev \  
libcurl3 \  
libcurl3-dev \  
libpng12-dev \  
libssl-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
  
# Added local Cache and Log Directory  
RUN mkdir -p /var/www/${APPLICATION_NAME} && chown -R www-data.www-data
/var/www/${APPLICATION_NAME} \  
&& mkdir -p /var/cache/${APPLICATION_NAME} && chown -R www-data.www-data
/var/cache/${APPLICATION_NAME} \  
&& mkdir -p /var/log/${APPLICATION_NAME} && chown -R www-data.www-data
/var/log/${APPLICATION_NAME}  
  
WORKDIR /var/www/${APPLICATION_NAME}  
  
VOLUME ["/var/www/${APPLICATION_NAME}"]  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/bin/supervisord"]  
  
EXPOSE 80  
######## SUPERVISORD DEPS ##########  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
supervisor\  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
COPY config/supervisord/config/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
  
######## END OF SUPERVISORD DEPS ##########  
######## BASE FPM DEPS ##########  
  
RUN mkdir -p $PHP_INI_DIR/conf.d  
  
RUN set -xe; \  
#\  
#fetchDeps=' \  
# wget \  
#'; \  
#apt-get update; \  
#apt-get install -y --no-install-recommends $fetchDeps; \  
#rm -rf /var/lib/apt/lists/*; \  
#\  
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
for key in $PHP_GPG_KEYS; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done; \  
gpg --batch --verify php.tar.xz.asc php.tar.xz; \  
rm -r "$GNUPGHOME"; \  
fi;  
  
#apt-get purge -y --auto-remove $fetchDeps  
  
COPY config/php-fpm/scripts/docker-php-source /usr/local/bin/  
  
RUN set -xe \  
&& buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
" \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
\  
&& docker-php-source extract \  
&& cd /usr/src/php \  
&& ./configure \  
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
$PHP_EXTRA_CONFIGURE_ARGS \  
&& make -j "$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& make clean \  
&& docker-php-source delete  
#\  
#&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps  
  
COPY config/php-fpm/scripts/docker-php-ext-* /usr/local/bin/  
  
  
RUN set -ex \  
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
echo 'clear_env = no'; \  
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
} | tee php-fpm.d/zz-docker.conf  
  
  
######## END OF BASE FPM DEPS ##########  
######## ADDITIONAL FPM DEPS ##########  
#RUN dpkg-reconfigure locales \  
# && locale-gen C.UTF-8 \  
# && /usr/sbin/update-locale LANG=C.UTF-8 \  
# && echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \  
# locale-gen  
  
RUN cd /tmp \  
&& wget http://www.ijg.org/files/jpegsrc.v9.tar.gz \  
&& tar xvfz jpegsrc.v9.tar.gz \  
&& cd jpeg-9 \  
&& ./configure \  
&& make \  
&& make install  
  
RUN cd /tmp \  
&& wget http://superb-
sea2.dl.sourceforge.net/project/freetype/freetype2/2.6.3/freetype-2.6.3.tar.gz
\  
&& tar xvfz freetype-2.6.3.tar.gz \  
&& cd freetype-2.6.3 \  
&& ./configure --without-png \  
&& make \  
&& make install  
  
# Environment Layer  
RUN pecl install mongodb \docker-php-source \  
&& echo "extension=mongodb.so" > $PHP_INI_DIR/conf.d/mongodb.ini \  
  
&& pecl install apcu \  
&& echo "extension=apcu.so" > $PHP_INI_DIR/conf.d/apcu.ini \  
  
&& pecl install redis \  
&& echo "extension=redis.so" > $PHP_INI_DIR/conf.d/redis.ini \  
&& rm -rf /tmp/pear \  
  
&& docker-php-ext-install zip intl mbstring gd exif bcmath pdo pdo_mysql
pdo_pgsql curl \  
&& docker-php-ext-enable opcache \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-jpeg-dir=/usr/local/lib --with-freetype-
dir=/usr/local/lib/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
######## END OF ADDITIONAL FPM DEPS ##########  
######## BASE NGINX DEPS ##########  
  
RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys $NGINX_GPG_KEY \  
&& echo "deb http://nginx.org/packages/ubuntu/ vivid nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y nginx=${NGINX_VERSION} \  
&& rm -rf /var/lib/apt/lists/*  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
ADD config/nginx/config/ /etc/nginx/  
  
######## END OF BASE NGINX DEPS ##########  

