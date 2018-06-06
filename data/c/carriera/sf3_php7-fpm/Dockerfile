FROM php:7.2  
MAINTAINER carriera  
  
# Install libxml2  
RUN apt-get update && apt-get install -y \  
libxml2 libxml2-dev  
  
# Install php extensions  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
zlib1g-dev \  
&& docker-php-ext-install -j$(nproc) iconv mbstring pdo_mysql soap zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
  
# Install git, unzip and wget  
RUN apt-get install -y git unzip wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
## Install Xdebug  
#RUN curl -fsSL 'https://xdebug.org/files/xdebug-2.5.5.tgz' -o xdebug.tar.gz \  
# && mkdir -p xdebug \  
# && tar -xf xdebug.tar.gz -C xdebug --strip-components=1 \  
# && rm xdebug.tar.gz \  
# && ( \  
# cd xdebug \  
# && phpize \  
# && ./configure --enable-xdebug \  
# && make -j$(nproc) \  
# && make install \  
# ) \  
# && rm -r xdebug \  
# && docker-php-ext-enable xdebug  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod a+x /usr/local/bin/composer  
  
# Install phpunit  
RUN wget https://phar.phpunit.de/phpunit-6.5.phar \  
&& chmod +x phpunit-6.5.phar \  
&& mv phpunit-6.5.phar /usr/local/bin/phpunit  
  
RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*  
  
WORKDIR /var/www/symfony  
  
CMD ["php-fpm", "-F"]  
  
EXPOSE 9000  

