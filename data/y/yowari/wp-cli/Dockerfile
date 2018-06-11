FROM php:apache  
MAINTAINER yowari  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
libjpeg-dev \  
libpng12-dev \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install gd mysqli opcache  
  
# set recommended PHP.ini settings  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN a2enmod rewrite expires  
  
RUN apt-get update --yes && \  
apt-get install --yes \  
mysql-client && \  
apt-get clean  
  
# install wp-cli in order to install, update, configure wordpress  
RUN curl -O 'https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar'  
RUN chmod +x wp-cli.phar  
RUN mv wp-cli.phar /usr/local/bin/wp  
  
# set where directory where wordpress will be installed  
WORKDIR /var/www/html/  
  
# download latest versino of wordpress  
RUN wp core download \  
\--allow-root \  
\--force  
  
COPY docker-entrypoint /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint"]  
CMD ["apache2-foreground"]  

