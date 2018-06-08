FROM php:7.1-fpm  
  
WORKDIR "/home/docker/eshop"  
  
# Install curl  
RUN apt-get -y install curl  
  
# Update sources list  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
# Upgrade  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y apt-utils  
  
# Install additional sofware  
RUN apt-get -y install git mc htop nodejs yarn  
  
# Install gulp  
RUN npm install gulp-cli -g  
RUN npm install gulp -g  
RUN npm install gulp-yarn --save-dev  
RUN npm install gulp-util  
  
# Install PHP extensions  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libmcrypt-dev \  
libxml2-dev \  
&& docker-php-ext-install pdo pdo_mysql mbstring gd iconv mcrypt zip xml  
RUN pecl install -o -f redis \  
&& docker-php-ext-enable redis  
  
RUN apt-get install -y sqlite3 libsqlite3-dev  
RUN docker-php-ext-install pdo_sqlite  
RUN docker-php-ext-install bcmath  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# XDebug  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
# Blackfire.io  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
  
# Clean for keep up small image  
RUN apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*

