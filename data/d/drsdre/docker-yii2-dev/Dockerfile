FROM drsdre/php-yii2:7.2-fpm-alpine  
  
MAINTAINER Andre Schuurman <docker@drsdre.org>  
  
LABEL Description="This image is PHP 7.2 FPM running on Alpine with extensions
needed for Yii2 application developement" Vendor="Andre Schuurman"
Version="7.2-fpm-dev-alpine"  
  
# Install the extensions  
RUN apk upgrade -U && apk add --update \  
git \  
vim \  
screen \  
wget \  
curl \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/main/ \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/community/ \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/  
  
# Install PHP PECL extensions  
RUN apk add --no-cache \  
$PHPIZE_DEPS \  
&& pecl install -o -f xdebug \  
&& rm -rf /tmp/pear \  
&& docker-php-ext-enable xdebug  
  
# add xdebug configurations  
RUN echo "error_reporting = E_ALL" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "display_startup_errors = On" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "display_errors = On" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.default_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_enable=1" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.remote_connect_back=0" >> /usr/local/etc/php/conf.d/docker-
php-ext-xdebug.ini \  
&& echo "xdebug.remote_port=9001" >> /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini \  
&& echo "xdebug.profiler_enable=1" >> /usr/local/etc/php/conf.d/docker-php-
ext-xdebug.ini \  
&& echo "xdebug.profiler_output_dir=/tmp/snapshots" >>
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini \  
&& echo "xdebug.profiler_enable_trigger=1" >>
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
  
# Add aliases for xdebug control  
RUN echo 'alias xoff="mv /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini
/usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini.off && kill -USR2 1"' >>
~/.bashrc  
RUN echo 'alias xon="mv /usr/local/etc/php/conf.d/docker-php-ext-
xdebug.ini.off /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && kill
-USR2 1"' >> ~/.bashrc  
  
# Cleanup  
RUN rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*

