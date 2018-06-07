# from https://www.drupal.org/requirements/php#drupalversions  
FROM php:5.6-apache  
MAINTAINER ya@donnu.edu.ua  
  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mbstring opcache pdo pdo_mysql pdo_pgsql zip  
  
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
  
WORKDIR /var/www/html  
  
# https://www.drupal.org/node/3060/release  
ENV DRUPAL_VERSION 8.0.3  
ENV DRUPAL_MD5 7d5f5278a870b8f4a29cda4fe915d619  
  
COPY . /var/www/html  
  
RUN chown -R www-data:www-data sites  
  
RUN \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer && \  
ln -s /usr/local/bin/composer /usr/bin/composer && \  
echo "deb http://httpredir.debian.org/debian jessie main contrib" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install git -y && \  
git clone \--depth 1 https://github.com/drush-ops/drush.git
/usr/local/src/drush && \  
ln -s /usr/local/src/drush/drush /usr/bin/drush && \  
cd /usr/local/src/drush && composer install

