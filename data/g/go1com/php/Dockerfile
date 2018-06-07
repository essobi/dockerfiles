FROM alpine:3.5  
# Build dependencies.  
ENV BUILD_DEPS \  
autoconf \  
file \  
g++ \  
gcc \  
libc-dev \  
make \  
pkgconf \  
re2c \  
git \  
php5-dev \  
php5-pear  
  
RUN cd /tmp \  
&& apk add --no-cache --virtual .build-deps $BUILD_DEPS \  
&& apk add --no-cache bash \  
apache2 \  
ca-certificates \  
wget \  
curl \  
icu-libs \  
git \  
pdftk \  
php5 \  
php5-cli \  
php5-apache2 \  
php5-bcmath \  
php5-bz2 \  
php5-calendar \  
php5-common \  
php5-ctype \  
php5-curl \  
php5-dom \  
php5-exif \  
php5-ftp \  
php5-gettext \  
php5-gd \  
php5-iconv \  
php5-intl \  
php5-imap \  
php5-json \  
php5-mailparse \  
php5-mysql \  
php5-mysqli \  
php5-mcrypt \  
php5-memcache \  
php5-opcache \  
php5-openssl \  
php5-pcntl \  
php5-pdo \  
php5-pdo_mysql \  
php5-pdo_pgsql \  
php5-pdo_sqlite \  
php5-phar \  
php5-posix \  
php5-pgsql \  
php5-shmop \  
php5-soap \  
php5-sockets \  
php5-sqlite3 \  
php5-sysvmsg \  
php5-sysvsem \  
php5-sysvshm \  
php5-wddx \  
php5-xml \  
php5-xmlreader \  
php5-xsl \  
php5-zip \  
php5-zlib \  
&& apk add --no-cache --virtual .xhprof-deps \  
graphviz \  
fontconfig \  
font-adobe-100dpi \  
&& git clone https://github.com/phacility/xhprof.git \  
&& ( \  
cd xhprof/extension \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
) \  
&& cd /tmp \  
&& wget https://pecl.php.net/get/uploadprogress -O uploadprogress.zip \  
&& tar -zxf uploadprogress.zip \  
&& ( \  
cd uploadprogress* \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& echo "extension=uploadprogress.so" >> /etc/php5/conf.d/uploadprogress.ini \  
) \  
&& echo "http://dl-cdn.alpinelinux.org/alpine/edge/community/" >>
/etc/apk/repositories \  
&& apk add --no-cache shadow \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /run/apache2 \  
&& groupmod -g 32 xfs && groupmod -g 33 www-data && usermod -u 106 -g www-data
-G apache apache \  
&& sed -ri \  
-e 's/Listen\ 80/#Listen\ 80/' \  
-e 's/#LoadModule\ rewrite_module/LoadModule\ rewrite_module/' \  
-e 's/#LoadModule\ remoteip_module/LoadModule\ remoteip_module/' \  
-e 's/#LoadModule\ expires_module/LoadModule\ expires_module/' \  
-e 's/#LoadModule\ logio_module/LoadModule\ logio_module/' \  
"/etc/apache2/httpd.conf" \  
&& apk del .build-deps \  
&& chown -R apache.www-data /tmp  
  
COPY rootfs /  
EXPOSE 80  
RUN chmod a+x /start.sh  
CMD ["/start.sh"]  

