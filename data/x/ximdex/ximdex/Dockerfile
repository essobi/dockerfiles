# Set the base image to use to Ubuntu  
FROM php:5.6-apache  
  
# Set the file maintainer  
MAINTAINER Ximdex ximdex  
  
# Enable Apache Rewrite Module  
RUN a2enmod rewrite  
  
# Updating the repository list  
RUN apt-get update && apt-get install -y unzip libicu-dev libcurl4-gnutls-dev
pwgen python-setuptools gettext libpng12-dev libmcrypt-dev libjpeg-dev
libxml2-dev libxslt-dev \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-configure sysvmsg \  
&& docker-php-ext-configure sysvsem \  
&& docker-php-ext-configure sysvshm \  
&& docker-php-ext-install pcntl sysvmsg sysvsem sysvshm gettext pdo pdo_mysql
curl xmlrpc gd intl xsl mcrypt opcache  
  
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
  
VOLUME /var/www/html  
  
COPY entrypoint.sh /entrypoint.sh  
COPY makedb.php /makedb.php  
  
# Cloning Ximdex CMS from GitHub in /var/www/html  
RUN curl -o ximdex.zip -SL https://github.com/XIMDEX/ximdex/archive/3.8.5.zip
&& \  
unzip ximdex.zip -d /usr/src/ && \  
mv /usr/src/ximdex-3.8.5 /usr/src/ximdex && \  
rm -f ximdex.zip && \  
# Setting permissions  
chown -R www-data:www-data /usr/src/ximdex && \  
chmod -R 2770 /usr/src/ximdex/data && \  
chmod -R 2770 /usr/src/ximdex/conf && \  
chmod -R 2770 /usr/src/ximdex/logs && \  
chmod 755 /entrypoint.sh && \  
touch /usr/local/etc/php/conf.d/docker-php-ext-prod.ini && \  
echo 'display_errors=0' > /usr/local/etc/php/conf.d/docker-php-ext-prod.ini  
  
EXPOSE 80  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

