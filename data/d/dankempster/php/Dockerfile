FROM php:alpine  
  
MAINTAINER dev@dankempster.co.uk  
  
RUN set -xe; \  
\  
apk add --update --virtual .build-deps \  
zlib-dev \  
libmcrypt-dev \  
libxml2-dev \  
openssl-dev \  
libxslt-dev \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
icu-dev \  
gettext-dev \  
; \  
\  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/; \  
docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd; \  
\  
docker-php-ext-install \  
pdo_mysql \  
gd \  
intl \  
dom \  
zip \  
mcrypt \  
bcmath \  
mbstring \  
gettext \  
xsl \  
; \  
\  
apk del .build-deps; \  
\  
apk add --update \  
libmcrypt \  
libxslt \  
freetype \  
libjpeg-turbo \  
libpng \  
libintl \  
icu \  
; \  
\  
rm -rf /var/cache/apk/*; \  
\  
mkdir /project; \  
chown -R www-data:www-data /project; \  
chmod -R 2775 /project;  
  
# Set PHP config  
COPY config/*.ini /usr/local/etc/php/conf.d/  
  
WORKDIR /project  

