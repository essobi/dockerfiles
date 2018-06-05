FROM php:7-apache  
MAINTAINER Michael Garrez <michael.garrez@gmail.com>  
  
ENV REFRESHED_AT 2015-09-23  
ENV PHP_INI_DIR /usr/local/etc/php  
ENV PHP_FILENAME php-7.0.2.tar.xz  
ENV PHP_EXTRA_BUILD_DEPS apache2-dev  
ENV PHP_VERSION 7.0.2  
ENV PHP_FILENAME php-7.0.2.tar.xz  
ENV PHP_SHA256
556121271a34c442b48e3d7fa3d3bbb4413d91897abbb92aaeced4a7df5f2ab2  
ENV PHP_EXTRA_CONFIGURE_ARGS --with-apxs2  
  
COPY config/php.ini /usr/local/etc/php/  
COPY bash /var  
  
RUN buildDeps=" \  
$PHP_EXTRA_BUILD_DEPS \  
libcurl4-openssl-dev \  
libreadline6-dev \  
librecode-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
xz-utils \  
" \  
&& set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& curl -fSL "http://php.net/get/$PHP_FILENAME/from/this/mirror" -o
"$PHP_FILENAME" \  
&& echo "$PHP_SHA256 *$PHP_FILENAME" | sha256sum -c - \  
&& curl -fSL "http://php.net/get/$PHP_FILENAME.asc/from/this/mirror" -o
"$PHP_FILENAME.asc" \  
&& gpg --verify "$PHP_FILENAME.asc" \  
&& mkdir -p /usr/src/php \  
&& tar -xf "$PHP_FILENAME" -C /usr/src/php --strip-components=1 \  
&& rm "$PHP_FILENAME"* \  
&& cd /usr/src/php \  
&& ./configure \  
\--with-config-file-path="$PHP_INI_DIR" \  
\--with-config-file-scan-dir="$PHP_INI_DIR/conf.d" \  
$PHP_EXTRA_CONFIGURE_ARGS \  
\--disable-cgi \  
\--enable-mysqlnd \  
\--with-curl \  
\--with-openssl \  
\--with-readline \  
\--with-recode \  
\--with-zlib \  
\--enable-sockets \  
&& make -j"$(nproc)" \  
&& make install \  
&& { find /usr/local/bin /usr/local/sbin -type f -executable -exec strip
--strip-all '{}' \+ || true; } \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps \  
&& make clean  
  
RUN apt-get update && apt-get install -y libmcrypt-dev zlib1g-dev vim cron
rsyslog git  
RUN docker-php-ext-install mysqli pdo pdo_mysql mbstring mcrypt iconv zip  
RUN pecl install channel://pecl.php.net/apcu_bc-1.0.3  
RUN docker-php-ext-enable apcu --ini-name 10-docker-php-ext-apcu.ini  
RUN docker-php-ext-enable apc --ini-name 20-docker-php-ext-apc.ini  
RUN a2enmod rewrite  
RUN usermod -u 1000 www-data  
RUN mkdir -p /var/www/html  
RUN apt-get update  
RUN yes | apt-get upgrade  
ENV TERM xterm  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN cd /var/www && git clone -b php7 https://github.com/phpredis/phpredis.git
&& cd /var/www/phpredis && phpize && ./configure && make && make install  
RUN echo "extension=redis.so" > /usr/local/etc/php/php.ini  
  
EXPOSE 80  
CMD ["/bin/bash", "/var/stack_start.sh"]  
ENTRYPOINT ["/bin/bash", "/var/stack_start.sh"]  

