FROM php:7.1-alpine  
MAINTAINER KASKO Tech Team <sysarch@kasko.io>  
  
WORKDIR /tmp  
  
RUN apk add --update --no-cache --virtual .phpize-deps \  
git \  
coreutils \  
freetype-dev \  
libjpeg-turbo-dev \  
libltdl \  
libmcrypt-dev \  
libpng-dev \  
imap-dev \  
openssl-dev \  
imagemagick-dev \  
libtool \  
$PHPIZE_DEPS && \  
apk add --update --no-cache imagemagick && \  
pecl install imagick && \  
docker-php-ext-enable imagick && \  
docker-php-ext-configure imap --with-imap --with-imap-ssl && \  
docker-php-ext-install imap && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php composer-setup.php --install-dir=/usr/bin --filename=composer && \  
php -r "unlink('composer-setup.php');" && \  
echo "{}" > composer.json && \  
composer config --no-interaction repositories.VisualCeption vcs
https://github.com/MatissJanis/VisualCeption.git && \  
composer require --prefer-source --no-interaction \  
"codeception/codeception:^2.2" \  
"codeception/visualception:dev-master" \  
"ahmedsamy/codeception-smtp-mail:^0.6.0" \  
"vlucas/phpdotenv:^2.4" && \  
ln -s /tmp/vendor/bin/codecept /usr/local/bin/codecept && \  
apk del git  
  
VOLUME ["/app"]  
  
WORKDIR /app  
  
ENTRYPOINT ["/usr/local/bin/codecept"]  
  
CMD ["--help"]  

