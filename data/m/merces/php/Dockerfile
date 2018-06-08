FROM php:7.1-fpm-alpine  
  
# PHP config  
ADD conf/symfony.ini /usr/local/etc/php/conf.d  
RUN apk update && apk add \  
zlib-dev \  
icu-dev \  
freetype-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
g++ \  
curl-dev \  
autoconf \  
make  
  
RUN docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& pecl install redis-3.1.3 \  
&& pecl install xdebug-2.5.0 \  
&& docker-php-ext-enable redis xdebug \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install intl pdo pdo_mysql zip mbstring curl  
  
# Install composer  
RUN curl -s https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install git  
RUN apk update && apk add git  
  
# Installing composer global dependencies  
ENV COMPOSER_HOME=/var/.composer  
RUN mkdir -p /var/.composer  
RUN chown -R www-data:www-data /var/.composer  
USER www-data  
RUN composer global --no-interaction require symfony/var-dumper
squizlabs/php_codesniffer phpmd/phpmd  
USER root  
RUN echo "auto_prepend_file=/var/.composer/vendor/autoload.php" >>
/usr/local/etc/php/conf.d/symfony.ini  
  
RUN mkdir -p /etc/phpcs/Merces  
ADD ruleset.xml /etc/phpcs/Merces  
RUN /var/.composer/vendor/bin/phpcs --config-set installed_paths
/etc/phpcs/Merces  
  
# use .ssh from local  
RUN mkdir -p /var/www/.composer  
RUN mkdir -p /var/www/.ssh  
VOLUME /var/www/.ssh  
  
# Entrypoint  
COPY entrypoint.sh /usr/local/bin/  
RUN ln -s /usr/local/bin/entrypoint.sh /entrypoint.sh && chmod +x
/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
  
CMD ["php-fpm"]  

