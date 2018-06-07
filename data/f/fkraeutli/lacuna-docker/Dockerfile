# Dockerfile adapted from: https://github.com/docker-
library/drupal/blob/2cbb3819480ebfa62053c75de2710659cbb8f66e/8.4-rc/apache/Dockerfile  
# from https://www.drupal.org/requirements/php#drupalversions  
FROM php:7.1-apache  
  
RUN a2enmod rewrite  
  
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
# PHP Warning: PHP Startup: Unable to load dynamic library
'/usr/local/lib/php/extensions/no-debug-non-zts-20151012/gd.so' -
libjpeg.so.62: cannot open shared object file: No such file or directory in
Unknown on line 0  
# PHP Warning: PHP Startup: Unable to load dynamic library
'/usr/local/lib/php/extensions/no-debug-non-zts-20151012/pdo_pgsql.so' -
libpq.so.5: cannot open shared object file: No such file or directory in
Unknown on line 0  
&& apt-mark manual \  
libjpeg62-turbo \  
libpq5 \  
&& apt-get purge -y --auto-remove $buildDeps  
  
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
  
RUN apt-get update && apt-get install -y unzip  
  
WORKDIR /var/www/html  
  
RUN curl -L https://github.com/PoeticMediaLab/LacunaStories/archive/master.zip
> master.zip  
RUN unzip master.zip && mv LacunaStories-master/* . && rm master.zip  
RUN cp ./sites/default/default.settings.php ./sites/default/settings.php  
RUN chmod a+w sites/default/files && chown -R www-data:www-data sites modules
themes  
  
EXPOSE 80  

