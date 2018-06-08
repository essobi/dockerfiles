FROM php:5.6-fpm  
LABEL maintainer "karolis@pretendentas.lt"  
  
RUN set -ex \  
&& apt-get update  
  
RUN set -ex \  
&& apt-get install -y \  
cron \  
g++ \  
git \  
libbz2-dev \  
libicu-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
libxslt-dev \  
zip \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -ex \  
&& docker-php-ext-configure gd --with-png-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure hash --with-mhash \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-configure mysql --with-mysql=mysqlnd \  
&& docker-php-ext-configure mysqli --with-mysqli=mysqlnd \  
&& docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql  
  
RUN set -ex \  
&& docker-php-ext-install -j$(nproc) \  
bcmath \  
bz2 \  
calendar \  
dba \  
exif \  
gd \  
gettext \  
intl \  
mcrypt \  
mysql \  
mysqli \  
opcache \  
pdo_mysql \  
pdo_pgsql \  
pgsql \  
shmop \  
soap \  
sockets \  
sysvmsg \  
sysvsem \  
sysvshm \  
wddx \  
xmlrpc \  
xsl \  
zip  
  
RUN set -ex \  
&& pecl install redis-3.1.3 xdebug-2.5.5 \  
&& docker-php-ext-enable redis xdebug  
  
RUN set -ex \  
&& mkdir -p /var/lib/php/session \  
&& mkdir -p /var/lib/php/wsdlcache \  
&& chown -R www-data:www-data /var/lib/php/session \  
&& chown -R www-data:www-data /var/lib/php/wsdlcache  
  
ENV GITHUB_TOKEN 87dc62834bd4267a86c4602b4efd381cfb6c8f14  
  
RUN set -ex \  
&& curl -sS https://getcomposer.org/installer | php -- \  
\--install-dir=/usr/bin \  
\--filename=composer \  
&& composer config -g github-oauth.github.com $GITHUB_TOKEN  
  
  
VOLUME /var/www/html  
WORKDIR /var/www/html  
  
EXPOSE 9000  
  
RUN set -x \  
addgroup -g 82 -S www-data \  
adduser -u 82 -D -S -G www-data www-data && exit 0  
  
COPY init.sh /init.sh  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["php-fpm"]  

