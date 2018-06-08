FROM php:7.1-fpm  
  
LABEL maintainer="slaci1@gmail.com"  
  
ARG locales='hu_HU.UTF-8 UTF-8\nen_US.UTF-8 UTF-8'  
ARG php_timezone="Europe/Budapest"  
ARG php_memory_limit="512M"  
ARG xdebug="0"  
  
RUN set -xe \  
&& DevDeps=" \  
libbz2-dev \  
libfreetype6-dev \  
libgmp-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libldap2-dev \  
libmagickwand-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
libxslt1-dev \  
zlib1g-dev" \  
&& Deps=" \  
locales \  
imagemagick-6.q16 \  
libfreetype6 \  
libjpeg62-turbo \  
libicu52 \  
libldap-2.4-2 \  
libmcrypt4 \  
libmemcached11 \  
libmemcachedutil2 \  
libpng12-0 \  
libpq5 \  
libltdl7 \  
libxslt1.1" \  
&& PeclModules=" \  
apcu \  
memcached \  
imagick \  
redis \  
igbinary \  
mongodb" \  
&& if [ "${xdebug}" = "1" ]; then PeclModules="${PeclModules} xdebug"; fi \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $Deps $DevDeps \  
&& echo $locales >> /etc/locale.gen \  
&& locale-gen \  
&& docker-php-ext-install -j$(nproc) \  
bz2 \  
bcmath \  
calendar \  
exif \  
gettext \  
gmp \  
iconv \  
intl \  
ldap \  
mcrypt \  
mysqli \  
opcache \  
pcntl \  
pdo_mysql \  
pdo_pgsql \  
shmop \  
soap \  
sockets \  
sysvmsg \  
sysvsem \  
sysvshm \  
xmlrpc \  
xsl \  
zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& pecl install $PeclModules \  
&& docker-php-ext-enable $PeclModules \  
&& echo "date.timezone = ${php_timezone}" >
"$PHP_INI_DIR/conf.d/001-timezone.ini" \  
&& echo "memory_limit = ${php_memory_limit}" >
"$PHP_INI_DIR/conf.d/002-memory-limit.ini" \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $DevDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY conf.d "$PHP_INI_DIR/conf.d/"  

