FROM alpine:3.7  
  
MAINTAINER docker@stefan-van-essen.nl  
  
ENV LANG='en_US.UTF-8' LANGUAGE='en_US.UTF-8' TERM='xterm'
DOCKER_HOST='docker'  
  
RUN apk -U --no-cache add \  
alpine-sdk \  
autoconf \  
automake \  
build-base \  
curl \  
docker \  
git \  
libjpeg-turbo \  
libjpeg-turbo-dev \  
libpng \  
libpng-dev \  
libwebp \  
libwebp-dev \  
make \  
nasm \  
nodejs-npm \  
openssh \  
php7 \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-fileinfo \  
php7-gettext \  
php7-gd \  
php7-gmp \  
php7-iconv \  
php7-json \  
php7-ldap \  
php7-mbstring \  
php7-mcrypt \  
php7-pcntl \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-phar \  
php7-redis \  
php7-session \  
php7-simplexml \  
php7-snmp \  
php7-tokenizer \  
php7-xdebug \  
php7-xml \  
php7-xmlreader \  
php7-xmlwriter \  
php7-zip \  
php7-zlib \  
&& curl --silent --show-error https://getcomposer.org/installer | php --
--install-dir=/usr/local/bin --filename=composer \  
&& npm install -g yarn \  
&& sed -i 's/;zend/zend/g' /etc/php7/conf.d/xdebug.ini  
  
COPY cache-tool.sh /usr/local/bin/cache-tool  

