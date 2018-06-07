FROM php:7.0-alpine  
MAINTAINER KASKO Tech Team <sysarch@kasko.io>  
  
WORKDIR /tmp  
  
RUN apk add --update --no-cache \  
git \  
coreutils \  
freetype-dev \  
libjpeg-turbo-dev \  
libltdl \  
libmcrypt-dev \  
libpng-dev \  
imap-dev \  
openssl-dev && \  
docker-php-ext-configure imap --with-imap --with-imap-ssl && \  
docker-php-ext-install imap && \  
docker-php-ext-install pcntl && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php composer-setup.php --install-dir=/usr/bin --filename=composer && \  
php -r "unlink('composer-setup.php');" && \  
composer require "phpunit/phpunit:~5.5.0" \--prefer-source --no-interaction &&
\  
composer require "phpunit/php-invoker" \--prefer-source --no-interaction && \  
ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit  
  
VOLUME ["/app"]  
  
WORKDIR /app  
  
ENTRYPOINT ["/usr/local/bin/phpunit"]  
  
CMD ["--help"]  

