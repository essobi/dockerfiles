FROM php:7.1.15-fpm  
  
MAINTAINER Gino Jongenelen <g.jongenelen@pushto.space>  
  
# Base image updates  
RUN apt-get update && apt-get upgrade -y && apt-get install automake git wget
libmcrypt-dev unzip libfreetype6-dev libjpeg62-turbo-dev libpng12-dev
libbz2-dev libtool libmosquitto-dev -y && apt-get clean  
# Ext installation  
RUN docker-php-ext-install pdo pdo_mysql iconv mbstring mysqli mcrypt bcmath
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && docker-php-ext-install gd bz2 zip  
  
# NgHttp2 installation  
RUN git clone https://github.com/tatsuhiro-t/nghttp2 && cd nghttp2 &&
autoreconf -i && automake && autoconf && ./configure --prefix=/usr && make &&
make install && cd .. && rm -rf nghttp2  
  
# Redis installation  
RUN wget https://github.com/phpredis/phpredis/archive/3.1.4.zip && unzip
3.1.4.zip && cd phpredis-3.1.4 && /usr/local/bin/phpize && ./configure --with-
php-config=/usr/local/bin/php-config && make && make install && \  
cd .. && rm -rf 3.1.4.zip phpredis-3.1.4  
  
ADD ./php.ini /usr/local/etc/php  
ADD ./start.sh /root  
  
# Mosquitto installation  
RUN pecl install Mosquitto-alpha && chmod +x /root/start.sh  
  
EXPOSE 9000  
CMD ["/root/start.sh"]

