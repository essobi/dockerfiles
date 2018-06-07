FROM php:7.1-fpm  
  
ARG VER_V8JS=1.3.3  
  
RUN set -ex \  
&& echo "deb http://us.archive.ubuntu.com/ubuntu/ wily main" >>
/etc/apt/sources.list \  
&& echo "deb http://ppa.launchpad.net/pinepain/libv8-5.2/ubuntu wily main " >>
/etc/apt/sources.list \  
&& echo "deb-src http://ppa.launchpad.net/pinepain/libv8-5.2/ubuntu wily main"
>> /etc/apt/sources.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
40976EAF437D05B5 3B4FE6ACC0B21F32 60C60AA4 \  
&& apt-get update && apt-get install -y git libgmp-dev libpq-dev libv8-5.2-dev
\  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/php7.tar.gz \  
&& curl -L -o /tmp/v8js.tar.gz
https://github.com/phpv8/v8js/archive/${VER_V8JS}.tar.gz \  
&& tar xfz /tmp/redis.tar.gz \  
&& tar xfz /tmp/v8js.tar.gz \  
&& mkdir -p /usr/src/php/ext \  
&& mv phpredis-php7 /usr/src/php/ext/redis \  
&& mv v8js-${VER_V8JS} /usr/src/php/ext/v8js \  
&& yes 'no' | pecl install -f apcu-5.1.5 \  
&& docker-php-ext-enable apcu \  
&& docker-php-ext-install v8js redis gmp pdo pdo_pgsql opcache zip \  
&& rm -rf /usr/src/php/ext/redis /tmp/redis.tar.gz /usr/src/php/ext/v8js
/tmp/v8js.tar.gz \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
COPY symfony.ini /usr/local/etc/php/conf.d/  
  
EXPOSE 9000  
CMD ["php-fpm"]  

