FROM php:5-fpm  
  
# install & cleanup  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libicu-dev \  
libz-dev libmemcached-dev \  
libffi-dev libssl-dev \  
zip cron && \  
apt-get -y clean && apt-get -y purge && rm -rf /var/lib/apt/lists/*  
  
RUN curl -fsSL 'http://www.imagemagick.org/download/ImageMagick.tar.gz' -o
ImageMagick.tar.gz && tar xvzf ImageMagick.tar.gz && \  
cd ImageMagick-* && ./configure && make && make install && /sbin/ldconfig
/usr/local/lib && \  
cd .. && rm -rf ImageMagick.tar.gz ImageMagick-*  
  
RUN docker-php-ext-configure mbstring && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd iconv mcrypt bcmath fileinfo intl gettext
zip && \  
pecl install memcache mongo imagick && \  
docker-php-ext-enable memcache mongo imagick  
  
WORKDIR /opt  
  
COPY ./entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["php-fpm"]

