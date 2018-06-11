FROM php:5.5-cli  
  
MAINTAINER Fred Cox "mcfedr@gmail.com"  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
libicu-dev \  
libxslt-dev \  
zlib1g-dev \  
libmemcached-dev \  
libmagickwand-dev \  
curl \  
git \  
&& apt-get autoremove -y \  
&& apt-get clean all  
  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install pcntl  
RUN docker-php-ext-install xsl  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install soap  
  
RUN pecl install -o -f redis-2.2.8 \  
&& rm -rf /tmp/pear  
RUN docker-php-ext-enable redis  
  
RUN pecl install -o -f xdebug \  
&& rm -rf /tmp/pear  
# RUN docker-php-ext-enable xdebug  
RUN pecl install -o -f apcu-4.0.11 \  
&& rm -rf /tmp/pear  
RUN docker-php-ext-enable apcu  
  
RUN pecl install -o -f memcached-2.2.0 \  
&& rm -rf /tmp/pear  
RUN docker-php-ext-enable memcached  
  
RUN pecl install -o -f imagick \  
&& rm -rf /tmp/pear  
RUN docker-php-ext-enable imagick  
  
RUN echo "date.timezone=UTC" > /usr/local/etc/php/conf.d/timezone.ini  
RUN echo "memory_limit=512M" > /usr/local/etc/php/conf.d/memory.ini  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN mkdir -p /opt/workspace  
WORKDIR /opt/workspace  

