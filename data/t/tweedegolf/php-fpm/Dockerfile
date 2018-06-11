FROM php:7.0.16-fpm  
  
RUN curl -s https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
\  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main" >
/etc/apt/sources.list.d/pgdg.list \  
&& apt-get update  
  
ENV POSTGRESQL_VERSION 9.6  
  
# Install other PHP modules  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libsqlite3-dev \  
sqlite3 \  
openssl \  
libssl-dev \  
libjpeg62-turbo-dev \  
libfreetype6-dev \  
libpng12-dev \  
postgresql-server-dev-$POSTGRESQL_VERSION \  
libxslt1-dev \  
libbz2-dev \  
libgmp-dev \  
libicu-dev \  
imagemagick \  
libmagickwand-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include --with-jpeg-
dir=/usr/include \  
&& docker-php-ext-install -j$(nproc) \  
gd \  
opcache \  
pdo_pgsql \  
zip \  
bcmath \  
bz2 \  
calendar \  
ftp \  
gettext \  
gmp \  
intl \  
pdo_mysql \  
pdo_sqlite \  
sockets \  
exif \  
&& pecl install imagick \  
&& pecl install apcu \  
&& docker-php-ext-enable \  
imagick \  
apcu  

