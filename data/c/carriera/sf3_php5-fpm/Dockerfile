FROM php:5-fpm  
MAINTAINER carriera  
  
# Install php extensions  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mbstring pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd calendar  
  
# Install git and unzip  
RUN apt-get install -y git unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Xdebug  
RUN curl -fsSL 'https://xdebug.org/files/xdebug-2.4.0.tgz' -o xdebug.tar.gz \  
&& mkdir -p xdebug \  
&& tar -xf xdebug.tar.gz -C xdebug --strip-components=1 \  
&& rm xdebug.tar.gz \  
&& ( \  
cd xdebug \  
&& phpize \  
&& ./configure --enable-xdebug \  
&& make -j$(nproc) \  
&& make install \  
) \  
&& rm -r xdebug \  
&& docker-php-ext-enable xdebug  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod a+x /usr/local/bin/composer  
  
RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*  
  
CMD ["php-fpm", "-F"]  
  
EXPOSE 9000  

