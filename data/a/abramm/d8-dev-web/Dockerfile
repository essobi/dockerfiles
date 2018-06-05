# This is mostly a copy-paste of drupal:8  
#  
# from https://www.drupal.org/requirements/php#drupalversions  
FROM php:5.6-apache  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev libpq-dev
wget mysql-client \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& pecl install xhprof-beta xdebug \  
&& docker-php-ext-enable xhprof xdebug \  
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
  
RUN wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture)" \  
&& chmod +x /usr/local/bin/gosu  
  
RUN cd /tmp && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
ADD https://github.com/drush-ops/drush/releases/download/8.0.1/drush.phar
/usr/local/bin/drush  
RUN chmod 755 /usr/local/bin/drush  
  
RUN echo "Europe/Kiev" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata  
  
WORKDIR /var/www/html  
VOLUME ["/var/www/html"]  
  
ADD entrypoint.sh /entrypoint.sh  
ADD download_drupal.sh /download_drupal.sh  
ADD logo.txt /usr/local/share/logo.txt  
  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  
  

