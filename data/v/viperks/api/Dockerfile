#  
# Basic php7-fpm box  
#  
FROM php:7-fpm  
  
# Composer version  
ENV COMPOSER_VERSION 1.1.2  
# Allow Composer to be run as root  
ENV COMPOSER_ALLOW_SUPERUSER 1  
# Install the PHP extensions we need plus composer  
RUN apt-get update && apt-get install -y \  
libcurl4-openssl-dev \  
libmagickwand-dev \  
mysql-client \  
ssh \  
&& pecl install xdebug \  
&& pecl install imagick \  
&& docker-php-ext-install \  
curl \  
opcache \  
pdo \  
pdo_mysql \  
&& docker-php-ext-enable imagick \  
&& curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=${COMPOSER_VERSION} && rm -rf /tmp/composer-
setup.php \  
&& curl -fsSL -o /usr/local/bin/phpunit "https://phar.phpunit.de/phpunit.phar"
\  
&& chmod +x /usr/local/bin/phpunit \  
&& apt-get -y clean \  
&& apt-get -y autoclean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/* || true \  
&& rm -rf && rm -rf /var/lib/cache/* && rm -rf /var/lib/log/* && rm -rf /tmp/*  
  
COPY php-fpm.conf /usr/local/etc/  
COPY php.ini /usr/local/etc/php/  

