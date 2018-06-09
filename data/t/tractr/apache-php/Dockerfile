FROM php:7.1-apache  
  
# Install other needed extensions  
RUN apt-get update && apt-get install -y libfreetype6 git-core mysql-client
ghostscript imagemagick libjpeg62-turbo libmcrypt4 libpng12-0 sendmail --no-
install-recommends && rm -rf /var/lib/apt/lists/*  
RUN buildDeps=" \  
libfreetype6-dev \  
libjpeg-dev \  
libldap2-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
libmagickwand-dev \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --enable-gd-native-ttf --with-jpeg-
dir=/usr/lib/x86_64-linux-gnu --with-png-dir=/usr/lib/x86_64-linux-gnu --with-
freetype-dir=/usr/lib/x86_64-linux-gnu \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install ldap \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install zip \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& apt-get purge -y --auto-remove $buildDeps  
# && cd /usr/src/php \  
# && make clean  
# Install x-debug  
# && curl -L https://pecl.php.net/get/xdebug-2.3.3.tgz >>
/usr/src/php/ext/xdebug.tgz \  
# && tar -xf /usr/src/php/ext/xdebug.tgz -C /usr/src/php/ext/ \  
# && rm /usr/src/php/ext/xdebug.tgz \  
# && docker-php-ext-install xdebug-2.3.3  
# Workaround for write permission on write to MacOS X volumes  
# See https://github.com/boot2docker/boot2docker/pull/534  
# RUN usermod -u 1000 www-data  

