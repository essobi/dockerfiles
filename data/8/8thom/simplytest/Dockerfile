FROM php:7.1-apache  
  
ENV APACHE_DOCUMENT_ROOT="/drupal/web/" \  
COMPOSER_ALLOW_SUPERUSER=1 \  
COMPOSER_CACHE_DIR=/composer/cache  
  
RUN sed -ri -e 's!/var/www/html!${APACHE_DOCUMENT_ROOT}!g' /etc/apache2/sites-
available/*.conf  
RUN sed -ri -e 's!/var/www/!${APACHE_DOCUMENT_ROOT}!g'
/etc/apache2/apache2.conf /etc/apache2/conf-available/*.conf  
  
RUN apt-get update && apt-get install -y \  
git \  
libcurl3-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpcre3-dev \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
mysql-client \  
zip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install -j$(nproc) \  
curl \  
gd \  
json \  
mbstring \  
mcrypt \  
mysqli \  
opcache \  
pdo_mysql \  
xml \  
&& a2enmod rewrite  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv /var/www/html/composer.phar /usr/bin/composer \  
&& chmod +x /usr/bin/composer \  
&& mkdir -p /composer/cache  
  
RUN curl -OL https://github.com/drush-ops/drush-
launcher/releases/download/0.5.0/drush.phar \  
&& mv drush.phar /usr/bin/drush \  
&& chmod +x /usr/bin/drush  

