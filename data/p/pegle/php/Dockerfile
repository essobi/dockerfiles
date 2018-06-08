FROM php:7.0-fpm-alpine  
  
# tools  
RUN apk add --no-cache \  
freetype \  
libpng \  
libjpeg-turbo \  
libxml2 \  
openssl \  
libmcrypt \  
icu \  
libxslt \  
# build deps  
&& apk add --no-cache --virtual .build-deps \  
freetype-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
libxml2-dev \  
libmcrypt-dev \  
icu-dev \  
libxslt-dev \  
# php config  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
# php extension  
&& docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) \  
gd \  
mysqli \  
pdo_mysql \  
soap \  
zip \  
mcrypt \  
intl \  
xsl \  
bcmath \  
# cleanup  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/* \  
&& apk del .build-deps \  
&& rm -rf tmp/* \  
  
# fpm port  
&& sed -i "s/:9000/:9001/" /usr/local/etc/php-fpm.d/www.conf \  
&& sed -i "s/:9000/:9001/" /usr/local/etc/php-fpm.d/zz-docker.conf \  
&& sed -i "s/:9000/:9001/" /usr/local/etc/php-fpm.d/www.conf.default  
  
COPY ./src/php.ini /usr/local/etc/php/php.ini  
  
EXPOSE 9001  

