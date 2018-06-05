FROM php:7-cli  
  
# The basics that drupal needs to function  
RUN apt-get update && apt-get install -y \  
libpng12-dev \  
libjpeg-dev \  
libpq-dev \  
\--no-install-recommends && rm -r /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
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
# It would be nice to install xdebug, but only enable it selectively per php
command (drush).  
# Also, composer run inside the container will complain.  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
# Install memcached so we can talk to a memcache server.  
# There isn't pecl support apprently for php7 memcache yet so we need to
compile ourselves.  
RUN apt-get update \  
&& buildDeps=" \  
git \  
libmemcached-dev \  
zlib1g-dev \  
" \  
&& doNotUninstall=" \  
libmemcached11 \  
libmemcachedutil2 \  
" \  
&& apt-get install -y $buildDeps \--no-install-recommends \  
&& rm -r /var/lib/apt/lists/* \  
\  
&& docker-php-source extract \  
&& git clone \--branch php7 https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached/ \  
&& docker-php-ext-install memcached \  
\  
&& docker-php-source delete \  
&& apt-mark manual $doNotUninstall \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false $buildDeps  
  
# Additional Packages for use as a cli container.  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
mysql-client \  
patch \  
pv \  
ruby-full \  
ssh-client \  
unzip \  
vim \  
wget \  
zip \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
# Install nodejs  
RUN \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs  
  
# Bundler  
RUN gem install bundler  
  
# Grunt, Bower  
RUN npm install -g grunt-cli bower  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Drush and Drupal Console  
RUN composer global require drush/drush:8.1.9 && \  
curl https://drupalconsole.com/installer -L -o drupal.phar && \  
mv drupal.phar /usr/local/bin/drupal  
  
# Install ahoy  
RUN wget -q https://github.com/devinci-
code/ahoy/releases/download/1.1.0/ahoy-`uname -s`-amd64 -O /usr/local/bin/ahoy
&& \  
chmod +x /usr/local/bin/ahoy  
  
# PHP settings changes can be saved in the following directory.  
# $PHP_INI_DIR/conf.d  
# Add Composer bin directory to PATH  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
# Home directory for bundle installs  
ENV BUNDLE_PATH .bundler  
  
# Mount the /var/www folder and allow it to be shared.  
ENV CODEROOT=/var/www  
VOLUME $CODEROOT  
  
# Update user ids to match OSX, so apache uses the correct UIDs for www-data.  
#RUN usermod -u 1000 www-data  
#RUN usermod -G staff www-data  
WORKDIR $CODEROOT  

