FROM php:latest  
  
MAINTAINER twosee <twose@qq.com>  
  
# set China timezone  
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo 'Asia/Shanghai' > /etc/timezone && \  
echo "[Date]\ndate.timezone=Asia/Shanghai" >
/usr/local/etc/php/conf.d/timezone.ini  
  
# install modules : GD iconv  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
openssl \  
libssh-dev \  
libpcre3 \  
libpcre3-dev \  
libnghttp2-dev \  
libhiredis-dev \  
curl \  
wget \  
zip \  
unzip \  
git && \  
apt autoremove && apt clean  
  
# install php pdo_mysql opcache  
# WARNING: Disable opcache-cli if you run you php  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ && \  
docker-php-ext-install \  
iconv \  
gd \  
pdo_mysql \  
mysqli \  
iconv \  
mbstring \  
json \  
opcache \  
sockets \  
pcntl && \  
echo "opcache.enable_cli=0" >> /usr/local/etc/php/conf.d/docker-php-ext-
opcache.ini  
  
#install redis  
RUN pecl install redis && docker-php-ext-enable redis  
  
# install composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
composer self-update --clean-backups  
  
# dev-tools for master  
RUN apt-get install -y gdb valgrind && \  
apt autoremove && apt clean

