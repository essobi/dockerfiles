FROM php:7-fpm  
MAINTAINER Shahriyar Imanov <shehi@imanov.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && apt-get install -y apt-utils && apt-get upgrade -y  
RUN apt-get install -y \  
git \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libmemcached-dev \  
libpng-dev \  
libpq-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
locales \  
locales-all \  
telnet \  
wget  
RUN docker-php-ext-install \  
bcmath \  
calendar \  
dom \  
exif \  
gettext \  
mbstring \  
opcache \  
pdo_mysql \  
pdo_pgsql \  
soap \  
sockets \  
xsl \  
zip  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
RUN pecl install -of mcrypt memcached \  
&& docker-php-ext-enable mcrypt memcached  
  
# Install Google's depot-tools  
#RUN apt-get install -y python libglib2.0-dev  
#RUN git clone
https://chromium.googlesource.com/chromium/tools/depot_tools.git /tmp/.depot-
tools  
#ENV PATH=$PATH:/tmp/.depot-tools  
# Fetch and compile v8  
#RUN cd /tmp \  
# && fetch v8 \  
# && cd v8 \  
# && git checkout 6.4.345 \  
# && gclient sync \  
# && tools/dev/v8gen.py -vv x64.release -- is_component_build=true \  
# && ninja -C out.gn/x64.release/ \  
# && mkdir -p /opt/v8/lib \  
# && mkdir -p /opt/v8/include \  
# && cp out.gn/x64.release/lib*.so out.gn/x64.release/*_blob.bin
out.gn/x64.release/icudtl.dat /opt/v8/lib/ \  
# && cp -R include/* /opt/v8/include/ \  
# && apt-get remove python -y  
# Compile php-v8js  
#RUN git clone --depth=1 https://github.com/phpv8/v8js.git /tmp/v8js \  
# && cd /tmp/v8js \  
# && phpize \  
# && ./configure --with-v8js=/opt/v8 LDFLAGS="-lstdc++"  
#ENV NO_INTERACTION 1  
#RUN cd /tmp/v8js \  
# && make \  
# && make test \  
# && make install \  
# && docker-php-ext-enable v8js  
# Install PECL php-mongodb  
RUN pecl install -of mongodb \  
&& rm -rf /tmp/pear \  
&& echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/mongo.ini  
  
# Install PECL php-xdebug  
RUN pecl install -of xdebug-2.6.0beta1 \  
&& rm -rf /tmp/pear \  
&& echo "zend_extension=xdebug.so" | tee /usr/local/etc/php/conf.d/xdebug.ini
\  
&& echo "xdebug.max_nesting_level = 1000" | tee -a
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.idekey = basisPhp" | tee -a
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable = 1" | tee -a
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_port = 54321" | tee -a
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_connect_back = 1" | tee -a
/usr/local/etc/php/conf.d/xdebug.ini  
  
# Install php-redis extension through Git  
RUN git clone https://github.com/phpredis/phpredis.git /tmp/phpredis \  
&& cd /tmp/phpredis \  
&& git checkout 3.1.4 \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /tmp/phpredis \  
&& echo "extension=redis.so" | tee /usr/local/etc/php/conf.d/redis.ini  
  
RUN php -m  
  
# Timezone  
RUN echo "date.timezone = UTC" | tee /usr/local/etc/php/conf.d/date.ini  
  
# Locale  
RUN locale-gen en_US.UTF-8 && locale-gen az_AZ.UTF-8 && locale-gen tr_TR.UTF-8
&& dpkg-reconfigure locales  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Clean-up  
RUN apt-get clean \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 54321  

