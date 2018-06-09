FROM php:5.6.30-fpm  
ENV NR_INSTALL_SILENT 1  
  
ADD ./php/php.ini /usr/local/etc/php/php.ini  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
wkhtmltopdf \  
xvfb \  
libxml2-dev \  
libpq-dev \  
libxslt-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install pdo \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install pdo_pgsql \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install xmlreader \  
&& docker-php-ext-install pgsql \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install pcntl \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install xsl \  
&& docker-php-ext-install sockets \  
&& docker-php-ext-install sysvmsg \  
&& docker-php-ext-install sysvsem \  
&& docker-php-ext-install sysvshm \  
&& docker-php-ext-install wddx \  
&& docker-php-ext-install shmop \  
&& docker-php-ext-install bcmath  
  
# Install xhprof as charlie god requested  
RUN pecl install -f xhprof && docker-php-ext-enable xhprof  
  
#RUN docker-php-ext-install mhash msgpack  
# Install newrelic php agent  
RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee
/etc/apt/sources.list.d/newrelic.list  
RUN curl https://download.newrelic.com/548C16BF.gpg | apt-key add -  
RUN apt-get update  
RUN apt-get install -y newrelic-php5  
RUN newrelic-install install  
  
# Install memcached  
# RUN apt-get update \  
# && apt-get install -y libmemcached11 libmemcachedutil2 build-essential
libmemcached-dev libz-dev \  
# && pecl install memcached \  
# && pecl install memcache \  
# && echo extension=memcached.so >> /usr/local/etc/php/conf.d/memcached.ini \  
# && echo extension=memcache.so >> /usr/local/etc/php/conf.d/memcache.ini \  
# && apt-get remove -y build-essential libmemcached-dev libz-dev \  
# && apt-get autoremove -y \  
# && apt-get clean \  
# && rm -rf /tmp/pear  
  
RUN apt-get update \  
&& apt-get install -y php5-memcached php5-memcache php5-mongo \  
&& mv /usr/lib/php5/20131226/memcache.so /usr/local/lib/php/extensions/no-
debug-non-zts-20131226/memcache.so \  
&& mv /usr/lib/php5/20131226/memcached.so /usr/local/lib/php/extensions/no-
debug-non-zts-20131226/memcached.so \  
&& mv /usr/lib/php5/20131226/mongo.so /usr/local/lib/php/extensions/no-debug-
non-zts-20131226/mongo.so \  
&& echo extension=memcached.so >> /usr/local/etc/php/conf.d/memcached.ini \  
&& echo extension=memcache.so >> /usr/local/etc/php/conf.d/memcache.ini \  
&& echo extension=mongo.so >> /usr/local/etc/php/conf.d/mongo.ini  
  
#upgrade mongo php extension to 1.6 to support auth  
RUN pecl upgrade mongo  
  
# Use 1000 UID user (web) to run php-fpm, so it has writable mount source code
folder, since ubuntu user UID is 1000 as well  
RUN useradd -m -u 1000 web  
  
# Clean up the rubbish  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
# Create php-fpm log directory  
RUN mkdir /var/log/php-fpm/  

