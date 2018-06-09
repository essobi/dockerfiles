FROM php:7-fpm-alpine  
LABEL maintainer Nathan Douglas <ndouglas@ainonline.com>  
COPY etc/php.ini /usr/local/etc/php/  
RUN set -xe \  
&& mkdir -p /app \  
&& apk add --no-cache \  
curl \  
curl-dev \  
freetype \  
freetype-dev \  
gettext \  
gettext-dev \  
icu-dev \  
inkscape \  
libcurl \  
libintl \  
libjpeg-turbo \  
libjpeg-turbo-dev \  
libmcrypt \  
libmcrypt-dev \  
libpng \  
libpng-dev \  
librsvg \  
libssl1.0 \  
libsodium-dev \  
libxml2 \  
libxml2-dev \  
mysql-client \  
perl \  
python3 \  
sqlite \  
sqlite-dev \  
zeromq \  
zlib \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-configure mbstring \  
\--enable-mbstring \  
&& docker-php-ext-configure pdo_sqlite \  
&& docker-php-ext-configure pdo_mysql \  
\--with-pdo-mysql \  
&& docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) \  
curl \  
gd \  
gettext \  
intl \  
mbstring \  
mcrypt \  
opcache \  
pdo_mysql \  
pdo_sqlite \  
xml \  
zip \  
&& python3 -m ensurepip \  
&& rm -rf /usr/lib/python*/ensurepip \  
&& pip3 install --upgrade pip setuptools \  
&& echo "php_admin_flag[log_errors] = On" >> /usr/local/etc/php-fpm.conf \  
&& echo "php_admin_value[error_reporting]=E_ALL" >> /usr/local/etc/php-
fpm.d/php-fpm.conf \  
&& echo "php_admin_flag[display_errors]=On" >> /usr/local/etc/php-fpm.d/php-
fpm.conf \  
&& echo "php_admin_flag[display_startup_errors]=On" >> /usr/local/etc/php-
fpm.d/php-fpm.conf \  
&& if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi \  
&& chown -R www-data:www-data /app \  
&& rm -rf /app/var/cache/* \  
&& echo Built successfully!  
VOLUME /app  
WORKDIR /app  

