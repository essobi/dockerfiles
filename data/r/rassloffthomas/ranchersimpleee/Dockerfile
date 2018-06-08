FROM php:7.2-fpm  
  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends \  
# required to install php-memcached and composer  
git \  
# required by gd  
libjpeg62-turbo-dev \  
# required by imagick  
libmagickwand-dev \  
# required by memcached  
libmemcached-dev \  
# required by gd  
libpng-dev \  
# required by pdo_mysql  
mysql-client \  
# required by composer  
openssl \  
# used to bundle PDFs, called directly via exec()  
pdftk \  
# required by composer  
unzip \  
# just for testing  
vim \  
# required by composer  
zip \  
# required by memcached  
zlib1g-dev \  
&& rm -r /var/lib/apt/lists/* \  
\  
&& docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ \--with-jpeg-dir=/usr/include/ \  
\  
&& docker-php-source extract \  
&& git clone --branch php7 https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached/ \  
\  
&& docker-php-ext-install \  
gd \  
mbstring \  
memcached \  
pdo_mysql \  
\  
&& pecl install \  
imagick \  
&& docker-php-ext-enable \  
imagick \  
\  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
\  
&& docker-php-source delete \  
&& apt-mark manual \  
libmemcached11 \  
libmemcachedutil2 \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false  
# add php config  
COPY config-server/php/php.ini /usr/local/etc/php/  
  
WORKDIR /var/www  
  
COPY . /var/www  
  
# laravel needs storage/framwork/views dir otherwise it throws that chache
path is not writeable  
# write permission for storage folder is also needed to store logs, cache and
uploaded files  
RUN mkdir -p storage/framework/views && \  
mkdir -p storage/app && \  
chown -R www-data:www-data storage  
  
RUN composer install --no-dev --no-progress

