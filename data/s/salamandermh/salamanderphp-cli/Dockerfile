FROM php:7.2.1-cli-alpine3.7  
# Packages  
RUN apk --update add \  
autoconf \  
build-base \  
linux-headers \  
libaio-dev \  
zlib-dev \  
curl \  
git \  
subversion \  
freetype-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libtool \  
libbz2 \  
bzip2 \  
bzip2-dev \  
libstdc++ \  
libxslt-dev \  
openldap-dev \  
imagemagick-dev \  
make \  
unzip \  
wget && \  
docker-php-ext-install bcmath zip bz2 pdo_mysql mysqli simplexml opcache
sockets mbstring pcntl xsl && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
pecl install imagick && \  
docker-php-ext-enable imagick && \  
pecl install redis && \  
docker-php-ext-enable redis && \  
pecl install swoole && \  
docker-php-ext-enable swoole && \  
docker-php-ext-install gd && \  
docker-php-ext-enable opcache && \  
apk del build-base \  
linux-headers \  
libaio-dev \  
&& rm -rf /var/cache/apk/*  
  
  
  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_VERSION 1.5.1  
  
  
RUN curl -s -f -L -o /tmp/installer.php
https://raw.githubusercontent.com/composer/getcomposer.org/da290238de6d63faace0343efbdd5aa9354332c5/web/installer
\  
&& php -r " \  
\$signature =
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410';
\  
\$hash = hash('SHA384', file_get_contents('/tmp/installer.php')); \  
if (!hash_equals(\$signature, \$hash)) { \  
unlink('/tmp/installer.php'); \  
echo 'Integrity check failed, installer is either corrupt or worse.' .
PHP_EOL; \  
exit(1); \  
}" \  
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
--version=${COMPOSER_VERSION} \  
&& rm /tmp/installer.php \  
&& composer --ansi --version --no-interaction  
  
VOLUME /var/www  
WORKDIR /var/www  
  
CMD [ "php", "./public/server.php" ]  

