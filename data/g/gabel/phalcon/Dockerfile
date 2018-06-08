FROM php:7.0-fpm  
MAINTAINER gabel <gabeldeluxe@gmail.com>  
  
ENV PHALCON_VERSION=3.0.3  
ENV TIMEZONE UTC  
ENV PHP_MEMORY_LIMIT 512M  
ENV MAX_UPLOAD 50M  
ENV PHP_MAX_FILE_UPLOAD 200  
ENV PHP_MAX_POST 100M  
  
# Compile Phalcon  
RUN set -xe && \  
curl -LO
https://github.com/phalcon/cphalcon/archive/v${PHALCON_VERSION}.tar.gz && \  
tar xzf v${PHALCON_VERSION}.tar.gz && cd cphalcon-${PHALCON_VERSION}/build &&
./install && \  
echo "extension=phalcon.so" > /usr/local/etc/php/conf.d/phalcon.ini && \  
cd ../.. && rm -rf v${PHALCON_VERSION}.tar.gz cphalcon-${PHALCON_VERSION} && \  
# Insall Phalcon Devtools, see https://github.com/phalcon/phalcon-devtools/  
curl -LO https://github.com/phalcon/phalcon-
devtools/archive/v${PHALCON_VERSION}.tar.gz && \  
tar xzf v${PHALCON_VERSION}.tar.gz && \  
mv phalcon-devtools-${PHALCON_VERSION} /usr/local/phalcon-devtools && \  
ln -s /usr/local/phalcon-devtools/phalcon.php /usr/local/bin/phalcon  
  
# Remove if not needed  
COPY config/php.ini /usr/local/etc/php/conf.d/  
  
# use proxy if needed  
# RUN pear config-set http_proxy $HTTP_PROXY  
RUN pecl install apcu && \  
docker-php-ext-enable apcu  
  
RUN docker-php-ext-install opcache  
  
RUN apt-get update && apt-get install -y zlib1g-dev \  
&& docker-php-ext-install zip  
  
RUN apt-get update && \  
apt-get install -y libssl-dev && \  
pecl install mongodb-1.2.5 && \  
docker-php-ext-enable mongodb  
  
RUN apt-get install -y zlib1g-dev libicu-dev libicu52 g++ \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install intl  
  
RUN apt-get purge -y --auto-remove libssl-dev libicu-dev zlib1g-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
# Make sure we're installing what we think we're installing!  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }" \  
&& php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --snapshot \  
&& rm -f /tmp/composer-setup.*  
  
CMD php-fpm -F -O 2>&1 | sed -u 's,.*: \"\\(.*\\)$,\1,'| sed -u 's,\"$,,' 1>&1

