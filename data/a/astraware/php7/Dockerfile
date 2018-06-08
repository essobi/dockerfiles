FROM php:7-fpm-alpine  
  
# Install dependencies  
RUN apk add --no-cache bash curl libmemcached-dev autoconf build-base zlib-dev
libmcrypt-dev geoip-dev subversion  
  
RUN docker-php-ext-install mysqli mcrypt opcache \  
&& pecl install apcu \  
&& docker-php-ext-enable apcu  
  
RUN curl -fsSL 'https://github.com/websupport-sk/pecl-
memcache/archive/NON_BLOCKING_IO_php7.zip' -o memcache.zip \  
&& unzip memcache.zip \  
&& rm memcache.zip \  
&& ( \  
cd pecl-memcache-NON_BLOCKING_IO_php7 \  
&& phpize \  
&& ./configure --enable-memcache \  
&& make \  
&& make install \  
) \  
&& rm -r pecl-memcache-NON_BLOCKING_IO_php7 \  
&& docker-php-ext-enable memcache  
  
RUN svn export -r 339679 http://svn.php.net/repository/pecl/geoip/trunk/ geoip
\  
&& ( \  
cd geoip \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
) \  
&& rm -r geoip \  
&& docker-php-ext-enable geoip  
  
# https://github.com/Yelp/dumb-init  
RUN curl -fsSL 'https://github.com/Yelp/dumb-
init/releases/download/v1.1.1/dumb-init_1.1.1_amd64' -o /usr/local/bin/dumb-
init  
RUN chmod +x /usr/local/bin/dumb-init  
  
ENV NR_INSTALL_SILENT=1  
ENV NR_INSTALL_KEY=5ab6d8b449801d72da4de3bcf1d3864ba3212299  
  
RUN curl -fsSL 'http://download.newrelic.com/php_agent/release/newrelic-
php5-6.4.0.163-linux-musl.tar.gz' -o newrelic.tar.gz \  
&& tar xvzf newrelic.tar.gz \  
&& rm newrelic.tar.gz \  
&& cp newrelic-php5-6.4.0.163-linux-musl/agent/x64/newrelic-20151012.so
/usr/local/lib/php/extensions/no-debug-non-zts-20151012/newrelic.so \  
&& cp newrelic-php5-6.4.0.163-linux-musl/daemon/newrelic-daemon.x64
/usr/bin/newrelic-daemon \  
&& mkdir -p /var/log/newrelic  
  
COPY php.ini /usr/local/etc/php/  
COPY newrelic.ini /usr/local/etc/php/conf.d/  
COPY docker.conf /usr/local/etc/php-fpm.d/  
  
EXPOSE 9000  
# Clean APK cache  
RUN rm -rf /var/cache/apk/*  
RUN apk del autoconf build-base subversion  
  
# Clear out old default site content  
RUN rm -rf /var/www/html/*  
  
RUN mkdir -p /opt/sites  
  
CMD ["dumb-init", "php-fpm"]

