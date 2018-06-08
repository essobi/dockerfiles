FROM php:7.1-alpine  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
  
RUN apk add -q --update curl git zip ca-certificates autoconf alpine-sdk
sqlite-dev && \  
update-ca-certificates && \  
pecl install xdebug && \  
docker-php-ext-enable xdebug && \  
docker-php-ext-install pdo_mysql && \  
docker-php-ext-install pdo_sqlite && \  
apk del autoconf alpine-sdk sqlite-dev && \  
rm -rf /var/cache/apk/* && \  
echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini && \  
echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini && \  
curl -o composer-setup.php https://getcomposer.org/installer && \  
curl -o composer-setup.sig https://composer.github.io/installer.sig && \  
php -r "if (hash('SHA384', file_get_contents('composer-setup.php')) !==
trim(file_get_contents('composer-setup.sig'))) { unlink('composer-setup.php');
echo 'Invalid installer' . PHP_EOL; exit(1); }" && \  
php composer-setup.php --quiet && \  
mv composer.phar /usr/local/bin && \  
composer.phar global -q require "hirak/prestissimo:^0.3" && \  
composer.phar global -q require "phpunit/phpunit:5.7 <6.0"  
  
ENV PATH /root/.composer/vendor/bin:$PATH  

