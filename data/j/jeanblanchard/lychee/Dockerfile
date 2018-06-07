FROM php:7.0-apache  
MAINTAINER Jean Blanchard <jean@blanchard.io>  
  
# Install Lychee  
ENV LYCHEE_VERSION v3.1.6  
# Configure php & dependencies  
RUN apt-get update &&\  
apt-get install -y zlib1g-dev libfreetype6-dev libjpeg62-turbo-dev
libpng12-dev libmagickwand-dev &&\  
rm -rf /var/lib/apt/lists/* &&\  
docker-php-ext-install -j$(nproc) exif mysqli zip &&\  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ &&\  
docker-php-ext-install -j$(nproc) gd &&\  
pecl install imagick &&\  
docker-php-ext-enable imagick  
ADD conf/php.ini /usr/local/etc/php/  
  
RUN curl -L
https://github.com/electerious/Lychee/archive/${LYCHEE_VERSION}.tar.gz | tar
-xzf - --strip 1 &&\  
chown -R www-data:www-data /var/www/html &&\  
chmod -R 770 /var/www/html &&\  
chmod -R 777 /var/www/html/uploads/ &&\  
chmod -R 777 /var/www/html/data/  
  
# Expose volumes  
RUN ln -s /var/www/html/uploads /uploads  
RUN ln -s /var/www/html/data /data  
  
VOLUME /uploads  
VOLUME /data  

