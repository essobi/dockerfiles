FROM php:7.0-apache  
  
MAINTAINER fredguile@gmail.com  
  
# Prerequisites  
RUN apt-get update && apt-get install -y \  
wget \  
git \  
rsync \  
supervisor \  
cmake \  
g++ \  
lua5.1 \  
liblua5.1-0-dev \  
libssl-dev \  
libxml2-dev \  
libcurl4-gnutls-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev  
  
# Configure PHP 7  
COPY config/php.ini /usr/local/etc/php/php.ini  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ && \  
docker-php-ext-install -j1 opcache \  
zip \  
ftp \  
xml \  
calendar \  
phar \  
ctype \  
json \  
mcrypt \  
iconv \  
session \  
pdo \  
pdo_mysql \  
soap \  
gd && \  
pecl install apcu-5.1.5 && docker-php-ext-enable apcu && a2enmod rewrite  
  
# Compile latest version of lsyncd  
RUN cd /tmp && git clone https://github.com/axkibe/lsyncd.git && \  
mkdir -p /tmp/lsyncd/build && \  
cd /tmp/lsyncd/build && \  
cmake .. && make && make install && \  
rm -rf /tmp/lsyncd  
  
# Configure lsynd  
RUN mkdir /etc/lsyncd  
  
COPY config/lsyncd.conf.lua /etc/lsyncd/lsyncd.conf.lua  
  
# Install IonCube  
COPY scripts/ioncube.sh /tmp/  
  
RUN chmod +x /tmp/ioncube.sh && /tmp/ioncube.sh  
  
# Clean up unnecessary packages  
RUN apt-get remove --purge -y \  
git \  
cmake \  
g++ && \  
apt-get autoremove --purge -y && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Required folders  
RUN mkdir -p /src /var/log/supervisor /var/log/lsyncd  
  
# Configure Supervisord  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

