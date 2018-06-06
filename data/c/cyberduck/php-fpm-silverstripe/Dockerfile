FROM php:7.0-fpm  
  
MAINTAINER clement@cyber-duck.co.uk  
  
RUN apt-get update && \  
apt-get install -y --force-yes --no-install-recommends \  
zlib1g-dev libicu-dev g++ \  
libz-dev \  
libpq-dev \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
openssh-server \  
git \  
cron \  
nano  
  
# Install the PHP zip extention  
RUN docker-php-ext-install zip  
  
# Install the PHP intl extention  
RUN docker-php-ext-configure intl  
RUN docker-php-ext-install intl  
  
# Install the PHP mysqli extention  
RUN docker-php-ext-install mysqli  
  
# Install the PHP pgsql extention  
RUN docker-php-ext-install pgsql  
  
# Install the PHP pdo_mysql extention  
RUN docker-php-ext-install pdo_mysql  
  
# Install the PHP pdo_pgsql extention  
RUN docker-php-ext-install pdo_pgsql  
  
#####################################  
# GD:  
#####################################  
  
# Install the PHP gd library  
RUN docker-php-ext-install gd && \  
docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd  
  
#####################################  
# TIDY:  
#####################################  
  
# Install the PHP tidy library  
RUN apt-get install -y libtidy-dev && \  
docker-php-ext-install tidy  
  
#####################################  
# xDebug:  
#####################################  
  
# Install the xdebug extension  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
# Copy xdebug configration for remote debugging  
COPY ./xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
  
#####################################  
# PHP OP Cache:  
#####################################  
  
# Install the php opcache extension  
RUN docker-php-ext-enable opcache  
# Copy opcache configration  
COPY ./opcache.ini /usr/local/etc/php/conf.d/opcache.ini  
  
#####################################  
# Composer:  
#####################################  
  
# Install composer and add its bin to the PATH.  
RUN curl -s http://getcomposer.org/installer | php && \  
echo "export PATH=${PATH}:/var/www/vendor/bin" >> ~/.bashrc && \  
mv composer.phar /usr/local/bin/composer  
# Source the bash  
RUN . ~/.bashrc  
  
#  
#--------------------------------------------------------------------------  
# Final Touch  
#--------------------------------------------------------------------------  
#  
  
ADD ./silverstripe.ini /usr/local/etc/php/conf.d  
  
#####################################  
# Aliases:  
#####################################  
# docker-compose exec php-fpm sake --> php
public/vendor/silverstripe/framework/cli-script  
RUN echo '#!/bin/bash\n/usr/local/bin/php
/var/www/public/vendor/silverstripe/framework/cli-script.php "$@"' >
/usr/bin/sake  
RUN chmod +x /usr/bin/sake  
# Deployer alias  
RUN echo '#!/bin/bash\n/usr/local/bin/php /var/www/vendor/bin/dep "$@"' >
/usr/bin/dep  
RUN chmod +x /usr/bin/dep  
  
RUN rm -r /var/lib/apt/lists/*  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www  
  
EXPOSE 9000  
  
CMD ["php-fpm"]  

