FROM php:7.2-cli  
MAINTAINER Chris Allan <chris@allan.codes>  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.21.4.0/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
RUN apt-get update -yqq \  
&& apt-get install git zlib1g-dev libsqlite3-dev procps -y \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install pdo_sqlite \  
&& docker-php-ext-install sockets  
  
RUN curl -fsSL https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer global require phpunit/phpunit ^6 --no-progress --no-scripts --no-
interaction \  
&& composer global require squizlabs/php_codesniffer ~3.3@dev --no-progress
--no-scripts --no-interaction \  
&& composer global require composer/satis --no-progress --no-scripts --no-
interaction  
  
RUN pecl install xdebug \  
&& echo 'zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20170718/xdebug.so' > \  
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
&& php -m | grep xdebug  
  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
ENTRYPOINT ["/init"]  
CMD ["/bin/bash"]

