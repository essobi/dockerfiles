# inspired by https://github.com/geertw/docker-php-ci/blob/master/php-7.1-no-
xdebug/Dockerfile  
  
FROM php:7.2  
  
RUN apt-get update  
RUN apt-get install -y libcurl4-openssl-dev sudo git libxslt-dev zlib1g-dev
graphviz zip libmcrypt-dev libicu-dev g++ libpcre3-dev libgd-dev
libfreetype6-dev sqlite  
RUN apt-get clean  
# libsodium  
##################  
RUN apt-get -y install curl build-essential unzip  
RUN mkdir -p /tmp-libsodium/libsodium && \  
cd /tmp-libsodium/libsodium && \  
curl -L
https://download.libsodium.org/libsodium/releases/libsodium-1.0.16.tar.gz -o
libsodium-1.0.16.tar.gz && \  
tar xfvz libsodium-1.0.16.tar.gz && \  
cd /tmp-libsodium/libsodium/libsodium-1.0.16/ && \  
./configure && \  
make && make check && \  
make install && \  
mv src/libsodium /usr/local/ && \  
rm -Rf /tmp-libsodium/  
  
RUN docker-php-ext-install sodium  
# libsodium >> end  
##################  
  
RUN docker-php-ext-install soap  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install xsl  
# mcrypt config:  
##################  
RUN apt-get -y install gcc make autoconf libc-dev pkg-config  
RUN pecl install --nodeps mcrypt-snapshot  
# mcrypt >> end  
##################  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install gettext  
RUN docker-php-ext-install curl  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install json  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install opcache  
  
RUN echo "memory_limit = -1;" > $PHP_INI_DIR/conf.d/memory_limit.ini  
  
ENV COMPOSER_ALLOW_SUPERUSER=1  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && composer global require
"fxp/composer-asset-plugin:^1.4.2"  

