FROM php:7.1-fpm  
  
ENV PHP_INI_DIR /usr/local/etc/php  
ENV PHP_MEMORY_LIMIT 500M  
  
RUN echo "memory_limit=$PHP_MEMORY_LIMIT" >
$PHP_INI_DIR/conf.d/memory_limit.ini  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
git \  
unzip \  
libmcrypt-dev \  
libicu-dev \  
libxml2-dev \  
# libmemcached11 \  
# libmemcachedutil2 \  
libmemcached-dev \  
libz-dev \  
openssh-client \  
&& docker-php-ext-install -j$(nproc) iconv intl xml soap mcrypt opcache pdo
pdo_mysql mysqli mbstring pcntl \  
&& git clone https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached \  
&& cd /usr/src/php/ext/memcached && git checkout -b php7 origin/php7 \  
&& docker-php-ext-configure memcached \  
&& docker-php-ext-install memcached \  
&& rm -rf /usr/src/php \  
&& rm -rf /var/lib/apt/lists/*  
  
#RUN echo "extension=memcached.so" > $PHP_INI_DIR/conf.d/memcached.ini  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#Remove de default html folder  
RUN rm -rf /var/www/html  
  
#Install NodeJs  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y --no-install-recommends nodejs \  
&& rm -rf /var/lib/apt/lists/*  
  
#Install Less  
RUN npm install -g less  

