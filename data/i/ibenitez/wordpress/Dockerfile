FROM php:7.0-cli as builder  
  
WORKDIR /app  
  
ARG COMPOSER_VERSION=1.4.2  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
git \  
ant \  
zip; \  
\  
rm -rf /var/lib/apt/lists/*; \  
\  
curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer --version=${COMPOSER_VERSION}; \  
\  
git clone \--depth 1 -b production-environment https://github.com/ismael-
benitez/wordpress-in-docker.git .; \  
\  
composer install --no-ansi --no-dev --no-interaction --no-progress --no-
scripts --optimize-autoloader;  
  
FROM php:7.0-apache  
  
WORKDIR /app  
  
# install the PHP extensions we need  
RUN set -ex; \  
\  
apt-get update; \  
apt-get install -y \  
zip \  
gettext-base \  
libjpeg-dev \  
libpng-dev \  
; \  
rm -rf /var/lib/apt/lists/*; \  
\  
docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr; \  
docker-php-ext-install gd mysqli opcache; \  
sed -i -e 's/<Directory \/var\/www\/>/<Directory \/app\/>/g'
/etc/apache2/apache2.conf;  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini; \  
\  
a2enmod rewrite expires;  
  
VOLUME /app/web/app/plugins  
VOLUME /app/web/app/themes  
VOLUME /app/web/app/uploads  
  
COPY \--from=builder /app/docker/prod/apache/wordpress.conf
/etc/apache2/sites-available/000-default.conf  
COPY \--from=builder /app/web/index.php /app/web/  
COPY \--from=builder /app/web/wp-config.php /app/web/  
COPY \--from=builder /app/web/wp /app/web/wp  
COPY \--from=builder /app/web/app/mu-plugins /app/web/app/mu-plugins  
COPY \--from=builder /app/config /app/config  
COPY \--from=builder /app/vendor /app/vendor  
COPY \--from=builder /app/docker/prod/apache/htaccess /app/web/.htaccess  
COPY \--from=builder /app/docker/prod/docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["apache2-foreground"]  

