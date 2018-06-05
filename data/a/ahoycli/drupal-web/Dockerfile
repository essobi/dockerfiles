FROM php:5.6-apache  
  
# Allow the DOCROOT to be configurable  
ENV DOCROOT=/var/www/docroot  
  
# Enable pretty urls in drupal.  
RUN a2enmod rewrite  
  
# The basics that drupal needs to function  
RUN apt-get update && apt-get install -y \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
&& docker-php-ext-configure gd \--with-png-dir=/usr \--with-jpeg-dir=/usr \  
&& docker-php-ext-install -j$(nproc) \  
gd \  
mbstring \  
opcache \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
zip  
  
# Setup a place for php to log errors. Turns out this isn't needed because  
# apache will log the php errors, but this is a handy example to get logs  
# out to work with docker logs commands.  
# RUN set -ex \  
# && . "$APACHE_ENVVARS" \  
# && ln -sfT /dev/stderr "$APACHE_LOG_DIR/php-error.log"  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
# Install memcached so we can talk to a memcache server.  
RUN apt-get update && apt-get install -y libmemcached-dev \  
&& pecl install memcached \  
&& docker-php-ext-enable memcached  
  
# Override the docroot of the base image with our own.  
RUN sed -i "s:/var/www/html:$DOCROOT:g" $APACHE_CONFDIR/sites-
available/000-default.conf  
  
# Mount the /var/www folder and allow it to be shared.  
VOLUME /var/www  
  
# Update user ids to match OSX, so apache uses the correct UIDs for www-data.  
RUN usermod -u 1000 www-data  
RUN usermod -G staff www-data  
  
WORKDIR $DOCROOT  

