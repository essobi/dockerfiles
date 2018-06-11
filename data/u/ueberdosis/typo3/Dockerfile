FROM php:7.1-fpm-alpine  
MAINTAINER Patrick Baber <patrick.baber@ueber.io>  
  
# URL: https://getcomposer.org/download/  
ENV COMPOSER_VERSION "1.4.1"  
# Install dependencies  
RUN apk add --update \  
imagemagick \  
openssl \  
wget \  
zlib \  
coreutils \  
freetype-dev \  
libjpeg-turbo-dev \  
libltdl \  
libmcrypt-dev \  
libpng-dev \  
libxml2-dev \  
&& \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) mysqli soap gd zip && \  
rm -rf /tmp/* /var/cache/apk/*  
  
# Configure PHP  
COPY /etc/php/conf.d/typo3.ini /usr/local/etc/php/conf.d/typo3.ini  
  
# Install Composer  
RUN wget https://getcomposer.org/download/${COMPOSER_VERSION}/composer.phar &&
\  
mv composer.phar /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer  
  
COPY src/composer.json /var/www/html/composer.json  
  
# Install TYPO3  
RUN cd /var/www/html && \  
composer install && \  
touch FIRST_INSTALL && \  
chown -R www-data. .  
  
WORKDIR /var/www/html  
  
VOLUME /var/www/html/fileadmin  
VOLUME /var/www/html/typo3conf

