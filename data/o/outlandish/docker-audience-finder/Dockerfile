FROM php:7.1-fpm  
  
RUN apt-get update  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \  
php -r "unlink('composer-setup.php');"  
  
RUN curl -OL
https://github.com/phpmetrics/PhpMetrics/releases/download/v2.3.2/phpmetrics.phar
&& \  
chmod +x phpmetrics.phar && \  
mv phpmetrics.phar /usr/local/bin/phpmetrics  
  
RUN curl -OL http://www.phpdoc.org/phpDocumentor.phar && \  
chmod +x phpDocumentor.phar && \  
mv phpDocumentor.phar /usr/local/bin/phpdoc  
  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.profiler_enable=1" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.profiler_enable_trigger=1" >>
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
&& echo "xdebug.profiler_output_dir=/app/profiling" >>
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
  
RUN echo "date.timezone=Europe/London" > /usr/local/etc/php/conf.d/zz-
custom.ini \  
&& echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/zz-custom.ini \  
&& echo "display_errors = on" >> /usr/local/etc/php/conf.d/zz-custom.ini \  
&& echo "session.autostart=0" >> /usr/local/etc/php/conf.d/zz-custom.ini  
  
ENV PATH "$PATH:/var/www/html/vendor/bin"  
RUN echo "env[\"XDEBUG_CONFIG\"] = \$XDEBUG_CONFIG" >> /usr/local/etc/php-
fpm.d/zz-docker.conf  
  
RUN docker-php-ext-install mysqli pdo pdo_mysql mbstring  
  
RUN apt-get install -y \  
libicu-dev \  
&& docker-php-ext-install intl \  
&& apt-get remove -y \  
libicu-dev \  
&& apt-get install -y \  
libicu57  
  
RUN apt-get install libcurl4-openssl-dev -y \  
&& docker-php-ext-install curl \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false libcurl4-openssl-dev -y  
  
RUN apt-get install libxml2-dev -y \  
&& docker-php-ext-install xml \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false libxml2-dev -y  
  
RUN apt-get install -y \  
zlib1g-dev \  
&& docker-php-ext-install zip \  
&& apt-get remove -y \  
zlib1g-dev \  
&& apt-get install -y \  
zlib1g  
  
RUN apt-get install -y \  
libmcrypt-dev \  
&& docker-php-ext-install mcrypt \  
&& apt-get remove -y \  
libmcrypt-dev \  
&& apt-get install -y \  
libmcrypt4  
  
RUN apt-get install -y --no-install-recommends libmagickwand-dev \  
&& pecl install imagick-3.4.3 \  
&& docker-php-ext-enable imagick  
  
#RUN apt-get update \  
# && apt-get install -y \  
# libmemcached-dev \  
# && pecl install memcached \  
# && echo "extension=memcached.so" > /usr/local/etc/php/conf.d/ext-
memcached.ini \  
# && apt-get remove -y \  
# libmemcached-dev \  
# && apt-get install -y \  
# libmemcached11 \  
# libmemcachedutil2 \  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends unzip libssl-
dev libpcre3 libpcre3-dev \  
&& cd /tmp \  
&& curl -sSL -o php7.zip https://github.com/websupport-sk/pecl-
memcache/archive/php7.zip \  
&& unzip php7 \  
&& cd pecl-memcache-php7 \  
&& /usr/local/bin/phpize \  
&& ./configure --with-php-config=/usr/local/bin/php-config \  
&& make \  
&& make install \  
&& echo "extension=memcache.so" > /usr/local/etc/php/conf.d/ext-memcache.ini \  
&& rm -rf /tmp/pecl-memcache-php7 php7.zip  
  
RUN docker-php-ext-configure opcache --enable-opcache \  
&& docker-php-ext-install opcache  
  
RUN apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/*  

