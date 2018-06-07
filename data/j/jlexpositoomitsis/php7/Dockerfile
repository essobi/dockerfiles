FROM php:7-fpm  
ENV XDEBUG_VERSION=2.5.0  
#IMAGE DEPENDENCIES  
#CRON NEEDED TO ADD WEB CRONTABS  
#MYSQL-CLIENT NEEDED FOR MAGERUN  
ENV ImageDeps="\  
cron \  
mysql-client \  
"  
# Install PHP7  
RUN buildDeps=" \  
libpng12-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libxml2-dev \  
freetype* \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $ImageDeps $buildDeps \--no-install-
recommends && rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure \  
gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir \  
&& docker-php-ext-install -j "$(getconf _NPROCESSORS_ONLN)" \  
gd \  
mbstring \  
mysqli \  
mcrypt \  
pdo_mysql \  
soap \  
zip \  
&& curl -s -L "http://xdebug.org/files/xdebug-${XDEBUG_VERSION}.tgz" | tar
-xvz -C /tmp \  
&& cd "/tmp/xdebug-${XDEBUG_VERSION}/" \  
&& phpize && ./configure --enable-xdebug && make \  
&& mkdir /usr/lib/php7/ && cp modules/xdebug.so /usr/lib/php7/xdebug.so \  
&& touch /usr/local/etc/php/ext-xdebug.ini \  
# Purge and delete tmp folders to reduce image size  
&& apt-get purge -y --auto-remove \  
&& rm -rf /tmp/*  
  
# Configure PHP  
COPY php.ini /usr/local/etc/php/php.ini  
COPY php-fpm.conf /usr/local/etc/  
COPY ext-xdebug.ini /usr/local/etc/php/conf.d/ext-xdebug.ini  
COPY crontab /etc/cron.d/magento-cron  
  
# Make sure the volume mount point is empty and Create the log file to be able
to run tail  
RUN rm -rf /var/www/html/* \  
&& touch /var/log/cron.log \  
&& chmod 777 /var/log/cron.log  
  
# Install magerun  
RUN curl -o magerun
https://raw.githubusercontent.com/netz98/n98-magerun/master/n98-magerun.phar
&& \  
chmod +x ./magerun && \  
cp ./magerun /usr/local/bin/ && \  
rm ./magerun  
  
#Install phpunit  
RUN curl -Lo phpunit.phar https://phar.phpunit.de/phpunit.phar \  
&& chmod +x phpunit.phar \  
&& mv phpunit.phar /usr/local/bin/phpunit  
  
ENV PHP_IDE_CONFIG="serverName=localhost"

