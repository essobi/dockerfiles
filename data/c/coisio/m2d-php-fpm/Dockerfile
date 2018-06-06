FROM php:7.0.7-fpm  
  
MAINTAINER Francois Raubenheimer <cois.io>  
  
# I go in this guy often so lets make sure it works  
ENV TERM=xterm  
  
RUN apt-get update \  
&& apt-get install -y \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
git  
  
RUN docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/  
  
RUN docker-php-ext-install \  
gd \  
intl \  
mbstring \  
mcrypt \  
pdo_mysql \  
xsl \  
zip  
  
COPY docker-php-pecl-install /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-php-pecl-install  
  
# Install redis with git will move to pecl soon  
RUN git clone https://github.com/phpredis/phpredis.git /tmp/phpredis \  
&& cd /tmp/phpredis \  
&& git checkout php7 \  
&& phpize \  
&& ./configure \  
&& make && make install \  
&& rm -rf /tmp/phpredis  
  
RUN docker-php-ext-enable redis  
  
ENV XDEBUG_VERSION 2.4.0  
RUN docker-php-pecl-install xdebug-$XDEBUG_VERSION && \  
echo
"xdebug.remote_enable=1\nxdebug.remote_port=\"9001\"\nxdebug.remote_connect_back=1\nxdebug.profiler_enable=0\nxdebug.profiler_enable_trigger=1"
> /usr/local/etc/php/conf.d/xdebug.ini \  
&& mkdir -p /usr/local/etc/php/xdebug.d \  
&& mv /usr/local/etc/php/conf.d/*xdebug.ini /usr/local/etc/php/xdebug.d/ \  
&& rm -rf /tmp/pear  
  
RUN docker-php-ext-enable xdebug  
  
COPY php.ini /usr/local/etc/php/  
  
WORKDIR /www  
  
EXPOSE 9000 9001  

