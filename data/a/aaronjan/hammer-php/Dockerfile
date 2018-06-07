#
==============================================================================  
# Hammer PHP  
# Docker PHP image on steroids.  
#  
# @license Apache-2.0  
#
==============================================================================  
FROM php:7.1-fpm-alpine  
LABEL maintainer="AaronJan <aaronjan@qq.com>"  
  
# create basic folders.  
# /web/application/ is for your project.  
RUN mkdir -p /web/application/ \  
# /web/config/ for all your configurations.  
&& mkdir -p /web/configs/ \  
# /web/scripts/ for executable scripts.  
&& mkdir -p /web/scripts/ \  
# /web/temp/ for temporary files.  
&& mkdir -p /web/temp/ \  
# /web/crontabs/ for Cron.  
&& mkdir -p /web/crontabs/ \  
# /root/.ssh/ for SSH stuff.  
&& mkdir -p ~/.ssh/ \  
# /var/log/supervisord/ for Supervisord's logs.  
&& mkdir -p /var/log/supervisord/  
  
# Copy configuration.  
COPY configs/supervisord.conf /web/configs/  
  
# Install necessary extensions.  
#  
RUN apk add --no-cache libjpeg-turbo-dev gmp-dev freetype-dev libpng-dev
openssh openssl-dev curl  
  
RUN apk add --no-cache --virtual .build-deps build-base autoconf zip unzip
libxml2-dev libmcrypt-dev wget \  
# install common extensions.  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& docker-php-ext-install -j${NPROC} zip soap pdo_mysql bcmath gmp \  
# GD extension must be configured manually.  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j${NPROC} gd \  
# these extension must be installed with PECL.  
&& pecl install mongodb ast \  
&& docker-php-ext-enable mongodb ast  
  
# Install utilities.  
#  
WORKDIR /web/temp  
  
# Supervisor providers extensibility, Cron lets you do task scheduling.  
RUN apk add --no-cache supervisor git vim rsync  
  
# Composer.  
COPY scripts/install_composer.sh /web/scripts/  
RUN sh /web/scripts/install_composer.sh \  
&& mv ./composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer  
  
# Clean up.  
RUN apk del .build-deps  
  
# Switch to your project folder.  
WORKDIR /web/application  
  
# Copy bin scripts  
COPY bin/with_ssh /usr/local/bin/  
RUN chmod +x /usr/local/bin/with_ssh  
  
# Start application using Supervisord.  
CMD ["/usr/bin/supervisord", "-c", "/web/configs/supervisord.conf"]

