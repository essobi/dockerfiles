FROM php:7.1.15-apache  
MAINTAINER Courtney <courtney@sellry.com>  
  
RUN requirements="libpng12-dev libmcrypt-dev libmcrypt4 libcurl3-dev
libfreetype6 libjpeg62-turbo libpng12-dev libfreetype6-dev libjpeg62-turbo-dev
imagemagick mysql-client-5.5 libxml2-dev curl git nodejs npm wget vim net-
tools procps libmagickwand-6.q16-dev" \  
&& apt-get update && apt-get upgrade -y && apt-get install -y $requirements &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install soap \  
&& docker-php-ext-install opcache \  
&& pecl install redis \  
&& pecl install imagick \  
&& pecl install lzf \  
&& docker-php-ext-enable redis imagick lzf \  
&& requirementsToRemove="libpng12-dev libmcrypt-dev libcurl3-dev libpng12-dev
libfreetype6-dev libjpeg62-turbo-dev" \  
&& apt-get purge --auto-remove -y $requirementsToRemove  
  
ENV N98_MAGERUN_URL https://files.magerun.net/n98-magerun.phar  
  
RUN curl -o /usr/local/bin/n98-magerun $N98_MAGERUN_URL \  
&& chmod +x /usr/local/bin/n98-magerun  
  
# New Relic  
RUN echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee
/etc/apt/sources.list.d/newrelic.list \  
&& wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add - \  
&& DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
newrelic-php5 && rm -rf /var/lib/apt/lists/*  
  
RUN a2dissite 000-default \  
&& a2disconf other-vhosts-access-log \  
&& a2enmod rewrite  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www/htdocs  

