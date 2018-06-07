###  
#  
# A simple image for running various PHP tools:  
# phpcs executable via /phpcs  
# phpunit executable via /phpunit  
# composer executable via /composer  
# phpdocumentor executable via /phpdoc  
#  
# The app should be mounted into /app to work  
#  
###  
FROM php:cli  
MAINTAINER Kingsquare <docker@kingsquare.nl>  
  
ENV TZ "Europe/Amsterdam"  
  
RUN apt-get update && \  
apt-get install \--no-install-recommends -qy git libmcrypt-dev zlib1g-dev && \  
apt-get autoremove -yq \--purge && \  
rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* && \  
docker-php-ext-install mcrypt && \  
docker-php-ext-install zip && \  
docker-php-ext-install mbstring && \  
pecl install xdebug && \  
echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20131226/xdebug.so" > /usr/local/etc/php/conf.d/xdebug.ini && \  
echo "date.timezone = $TZ" > /usr/local/etc/php/conf.d/timezone.ini  
  
RUN curl -o /phpunit https://phar.phpunit.de/phpunit.phar && \  
curl -o /phpcs https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar && \  
curl -o /phpdoc http://phpdoc.org/phpDocumentor.phar && \  
curl -o /composer https://getcomposer.org/composer.phar && \  
chmod +x /phpunit /phpcs /composer /phpdoc  
  
WORKDIR /app  
VOLUME ["/app"]

