FROM php:7-apache  
  
LABEL description="Apache PHP stack for WordPress" vendor="21st digital"
version="1.0"  
# install the PHP extensions we need  
RUN set -ex; \  
\  
savedAptMark="$(apt-mark showmanual)"; \  
\  
apt-get update; \  
apt-get install -y --no-install-recommends \  
libjpeg-dev \  
libpng-dev \  
libmemcached-dev \  
libtidy-dev \  
zlib1g-dev \  
; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install gd mysqli opcache tidy; \  
pecl install xdebug memcached redis; \  
docker-php-ext-enable xdebug memcached redis; \  
\  
# reset apt-mark's "manual" list so that "purge --auto-remove" will remove all
build dependencies  
apt-mark auto '.*' > /dev/null; \  
apt-mark manual $savedAptMark; \  
ldd "$(php -r 'echo ini_get("extension_dir");')"/*.so \  
| awk '/=>/ { print $3 }' \  
| sort -u \  
| xargs -r dpkg-query -S \  
| cut -d: -f1 \  
| sort -u \  
| xargs -rt apt-mark manual; \  
\  
apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false;
\  
rm -rf /var/lib/apt/lists/*  
  
COPY ./apache/bedrock.conf /etc/apache2/sites-available/bedrock.conf  
COPY ./php/bedrock-php.dev.ini /usr/local/etc/php/conf.d/bedrock-php.ini  
  
RUN a2dissite 000-default && a2ensite bedrock  
  
RUN a2enmod rewrite expires headers ext_filter

