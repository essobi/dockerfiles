FROM php:5.6-fpm  
  
MAINTAINER simone@cyber-duck.co.uk  
  
ENV XDEBUG "false"  
  
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
nano \  
curl \  
libcurl4-openssl-dev  
  
# Install the PHP curl extention  
RUN if [ ! -d /usr/include/curl ]; then \  
ln -sT "/usr/include/$debMultiarch/curl" /usr/local/include/curl; \  
fi;  
  
RUN docker-php-ext-install curl  
  
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
# xDebug:  
#####################################  
  
# Install the xdebug extension  
RUN pecl install xdebug-2.5.5  
RUN if [ "$XDEBUG" = "true" ]; then \  
docker-php-ext-enable xdebug; \  
fi  
  
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
  
#####################################  
# Drush:  
#####################################  
RUN composer global require drush/drush:8.x  
  
#--------------------------------------------------------------------------  
# Final Touch  
#--------------------------------------------------------------------------  
ADD ./drupal.ini /usr/local/etc/php/conf.d  
  
#####################################  
# Aliases:  
#####################################  
  
# Deployer alias  
RUN echo '#!/bin/bash\n/usr/local/bin/php /var/www/vendor/bin/dep "$@"' >
/usr/bin/dep  
RUN chmod +x /usr/bin/dep  
  
RUN rm -r /var/lib/apt/lists/*  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www  
  
EXPOSE 9000  
  
CMD ["php-fpm"]  

