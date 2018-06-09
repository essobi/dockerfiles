FROM php:5.6-fpm-alpine  
  
ENV TMP_APP=/tmp/app  
  
# Install  
RUN apk add --update \--no-cache --virtual .ext-deps \  
autoconf gcc g++ make \  
curl \  
openssl \  
libjpeg-turbo-dev \  
libwebp-dev \  
libpng-dev \  
freetype-dev \  
libmcrypt-dev && \  
  
set -x && \  
docker-php-ext-configure gd \  
\--with-jpeg-dir=/usr/include \--with-png-dir=/usr/include \--with-webp-
dir=/usr/include \--with-freetype-dir=/usr/include && \  
docker-php-ext-install \  
gd \  
mbstring \  
mysqli \  
mcrypt \  
mysql \  
opcache \  
pdo_mysql \  
zip && \  
  
# Install igbinary  
cd /tmp && \  
wget https://github.com/igbinary/igbinary/archive/2.0.4.zip && \  
unzip 2.0.4.zip && cd igbinary-2.0.4 && \  
phpize && ./configure && \  
make && make install && \  
echo extension=igbinary.so >> /usr/local/etc/php/conf.d/igbinary.ini && \  
cd ../ && rm -rf igbinary-2.0.4 && \  
  
#apk add --no-cache --virtual .mongodb-ext-build-deps openssl-dev && \  
pecl install redis && \  
#pecl install mongodb && \  
pecl clear-cache && \  
#apk del .mongodb-ext-build-deps  
  
docker-php-ext-enable redis.so && \  
#docker-php-ext-enable mongodb.so && \  
  
apk del autoconf gcc g++ make && \  
docker-php-source delete  
  
# Install Configure & App  
COPY . ${TMP_APP}  
  
# Build Application  
RUN set -x && \  
yes | cp -rf ${TMP_APP}/config/php-config.ini
/usr/local/etc/php/conf.d/config.ini && \  
yes | cp -rf ${TMP_APP}/config/php-fpm.conf /usr/local/etc/ && \  
rm -rf ${TMP_APP}  

