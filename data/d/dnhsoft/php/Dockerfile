FROM php:7.2-apache  
  
RUN apt-get update && apt-get install -y \  
git \  
wget \  
mysql-client \  
libmcrypt-dev \  
libicu-dev \  
zlib1g-dev  
  
RUN pecl install apcu  
  
# install pdo  
RUN /usr/local/bin/docker-php-ext-install pdo pdo_mysql  
  
# install intl  
RUN docker-php-ext-install intl  
  
# install zip  
RUN /usr/local/bin/docker-php-ext-install zip  
  
RUN a2enmod rewrite  
  
# useful for local development with mounted sources  
RUN sed -i 's/www-data:x:33:33/www-data:x:1000:1000/g' /etc/passwd  
  
WORKDIR /app  
  
RUN chown -R www-data:www-data /app  
  
RUN mkdir -p /app/public && rm -rf /var/www/html && ln -s /app/public
/var/www/html  
  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
COPY setup-php.sh /setup-php.sh  
  
# some default values of php variables  
ENV PHP_UPLOAD_MAX_FILESIZE "64M"  
ENV PHP_POST_MAX_FILESIZE "64M"  
ENV PHP_MEMORY_LIMIT "1024M"  
ENV PHP_MAX_EXECUTION_TIME "60"  
# opcache variables  
ENV PHP_OPCACHE_ENABLE 1  
ENV PHP_OPCACHE_MEMORY_CONSUMPTION 128  
ENV PHP_OPCACHE_INTERNED_STRINGS_BUFFER 8  
ENV PHP_OPCACHE_ACCELERATED_FILES 10000  
ENV PHP_OPCACHE_REVALIDATE_FREQ 5  
ENV PHP_OPCACHE_FAST_SHUTDOWN 1  
ENV PHP_SESSION_COOKIE_SECURE On  
  
# other variables  
ENV PHP_APCU_ENABLE 1  
RUN sed -i "3i/setup-php.sh" /usr/local/bin/apache2-foreground  

