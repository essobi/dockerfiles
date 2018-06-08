# from https://www.drupal.org/requirements/php#drupalversions  
FROM php:7.1-fpm  
  
# install the PHP extensions we need  
RUN set -ex \  
&& buildDeps=' \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libpq-dev \  
' \  
&& apt-get update && apt-get install -y --no-install-recommends $buildDeps &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd \  
\--with-jpeg-dir=/usr \  
\--with-png-dir=/usr \  
&& docker-php-ext-install -j "$(nproc)" gd mbstring opcache pdo pdo_mysql
pdo_pgsql zip \  
&& apt-mark manual \  
libjpeg62-turbo \  
libpq5 \  
&& apt-get purge -y --auto-remove $buildDeps  
  
RUN apt-get update && apt-get install -y mysql-client  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
# set upload size to 10M  
RUN { \  
echo 'upload_max_filesize = 10M'; \  
echo 'post_max_size = 10M'; \  
} > /usr/local/etc/php/conf.d/upload-size.ini  
  

