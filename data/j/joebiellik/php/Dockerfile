FROM php:fpm  
  
# Install extensions  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y libicu-dev --no-install-recommends \  
&& docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \  
&& docker-php-ext-install -j$(nproc) pdo_mysql mysqli calendar intl \  
&& apt-get purge -y --auto-remove libicu-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Configure production php.ini  
RUN curl -sS https://raw.githubusercontent.com/php/php-src/master/php.ini-
production \  
| sed -e 's/^;\(date.timezone.*\)/\1 \"Etc\/UTC\"/' \  
-e 's/^\(upload_max_filesize =\).*/\1 25M/' \  
-e 's/^\(post_max_size =\).*/\1 25M/' \  
> /usr/local/etc/php/php.ini  

