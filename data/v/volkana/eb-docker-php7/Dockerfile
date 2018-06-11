FROM php:7.0.8-fpm  
  
COPY config/custom.ini /usr/local/etc/php/conf.d/  
  
RUN apt-get update && apt-get install -y zlib1g-dev libicu-dev libpq-dev wget
git libmemcached-dev \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install zip  
  
# install memcached extension  
RUN git clone \--branch php7 https://github.com/php-memcached-dev/php-
memcached /usr/src/php/ext/memcached \  
&& cd /usr/src/php/ext/memcached \  
&& docker-php-ext-configure memcached \  
&& docker-php-ext-install memcached  
  
RUN mkdir -p /opt/newrelic  
WORKDIR /opt/newrelic  
  
RUN wget http://download.newrelic.com/php_agent/release/newrelic-
php5-6.4.0.163-linux.tar.gz -O newrelic-php5-linux.tar.gz  
RUN tar -zxf newrelic-php5-linux.tar.gz  
  
ENV NR_INSTALL_SILENT true  
ENV NR_INSTALL_PHPLIST /usr/local/bin  
  
WORKDIR /opt/newrelic/newrelic-php5-6.4.0.163-linux  
RUN bash newrelic-install install  
RUN mkdir -p /var/log/newrelic  
RUN mkdir -p /var/run/newrelic  
  
WORKDIR /var/www/html  
  
RUN usermod -u 1000 www-data

