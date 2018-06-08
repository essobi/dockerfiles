FROM php:7.1-fpm  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends libmagickwand-dev libicu-dev
gettext libz-dev libmemcached-dev libjpeg62-turbo libjpeg62-turbo-dev
libpng12-0 libpng12-dev libxpm4 libxpm-dev libfreetype6-dev libxml2-dev pkg-
config libcurl4-openssl-dev libssl-dev \  
&& pecl install xdebug-2.5.5 \  
&& pecl install imagick-3.4.3 \  
&& docker-php-ext-enable imagick \  
&& docker-php-ext-enable opcache \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install pcntl \  
&& docker-php-ext-install intl \  
&& pecl install igbinary memcached \  
&& docker-php-ext-enable igbinary memcached \  
&& docker-php-ext-install bcmath \  
&& pecl install mongodb \  
&& docker-php-ext-enable mongodb \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ --with-xpm-dir=/usr/include/ \  
&& docker-php-ext-install gd \  
# Profiling tool tideways  
&& echo 'deb http://s3-eu-west-1.amazonaws.com/qafoo-profiler/packages debian
main' > /etc/apt/sources.list.d/tideways.list \  
&& apt-get install -y wget \  
&& wget -qO - https://s3-eu-west-1.amazonaws.com/qafoo-
profiler/packages/EEB5E8F4.gpg | apt-key add \- \  
&& apt-get update \  
&& apt-get install tideways-php \  
&& apt-get clean \  
&& pecl clear-cache \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY profiling.ini /usr/local/etc/php/conf.d/profiling.ini.deactivated  
  
COPY entryscript.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entryscript.sh  
ENTRYPOINT ["entryscript.sh"]

