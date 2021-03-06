FROM phusion/baseimage:0.9.18  
  
MAINTAINER Reload A/S <kontakt@reload.dk>  
  
COPY files/etc/ /etc/  
# Add our tools to PATH.  
COPY files/bin /usr/local/bin/  
  
ENV PATH /root/.composer/vendor/bin:$PATH  
ENV PHP_VERSION 5.6  
  
RUN \  
apt-get update && \  
# Install packages needed to enable an extra repository.  
DEBIAN_FRONTEND=noninteractive apt-get -y install python-software-properties
&& \  
# Add a repo that contains php ${PHP_VERSION}  
LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && \  
# Do the remaining installation of packages.  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
apache2 \  
# Drush needs this to work  
mysql-client \  
libapache2-mod-php${PHP_VERSION} \  
# Default extensions.  
php${PHP_VERSION}-curl \  
php${PHP_VERSION}-gd \  
php${PHP_VERSION}-mysql \  
php${PHP_VERSION}-xml \  
php${PHP_VERSION}-xdebug \  
php${PHP_VERSION}-xhprof \  
php${PHP_VERSION}-mbstring \  
php${PHP_VERSION}-mcrypt \  
php${PHP_VERSION}-soap \  
# Added for installing composer.  
php${PHP_VERSION}-zip \  
# Other extensions  
php${PHP_VERSION}-intl \  
php-memcache \  
php-memcached \  
# For default snakeoil certificates which SSL is configuered to use  
# per default in Apache.  
ssl-cert \  
dnsutils \  
imagemagick \  
unzip && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY files/etc-post/ports.conf /etc/apache2/  
  
RUN \  
a2enmod headers && \  
a2enmod rewrite && \  
a2enmod ssl && \  
a2enmod proxy && \  
a2enmod proxy_http && \  
a2ensite default-ssl && \  
a2enconf drupal && \  
phpenmod drupal-recommended && \  
phpdismod xdebug && \  
# Drush 8 is the current stable that supports Drupal version 6, 7 and 8.  
curl -sS https://getcomposer.org/installer | sudo php -- --install-
dir=/usr/local/bin --filename=composer && \  
composer global require drush/drush:8.* && \  
rm -rf /tmp/* /var/tmp/*  
  
ENV PHP_DEFAULT_EXTENSIONS calendar ctype curl dom exif fileinfo ftp gd
gettext iconv json mcrypt mysql mysqli mysqlnd opcache pdo pdo_mysql phar
posix readline shmop simplexml soap sockets sysvmsg sysvsem sysvshm tokenizer
wddx xhprof xml xmlreader xmlwriter xsl mbstring zip  
  
EXPOSE 80 443  
WORKDIR /var/www/html  

