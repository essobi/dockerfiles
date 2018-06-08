# PixelHyperlink PHP 7.0 Server Docker  
#  
# VERSION 1.5.0  
FROM pixelhyperlinkdockers/apacheserver:v1.1.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with apache and php
service using fpm and proxy."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.5.0"  
LABEL com.pixelhyperlink.docker.phpserver.version="1.5.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.phpserver.release-date="2017-07-05"  
LABEL com.pixelhyperlink.docker.phpserver.version.is-production="true"  
  
# RUN apt-cache pkgnames | grep php7.1  
ENV BUILD_ENV production  
ENV PHP_VERSION 7.1  
ENV PHP_EXT_VERSION 7.1  
ENV REQUIRES_PHP_SETUP 1  
# Install apache, PHP, and supplimentary programs.  
RUN add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install php$PHP_VERSION \  
php$PHP_VERSION-bz2 \  
php$PHP_EXT_VERSION-cli \  
php$PHP_EXT_VERSION-common \  
php$PHP_EXT_VERSION-curl \  
php$PHP_EXT_VERSION-fpm \  
php$PHP_EXT_VERSION-gd \  
php$PHP_EXT_VERSION-imap \  
php$PHP_EXT_VERSION-intl \  
php$PHP_EXT_VERSION-json \  
php$PHP_EXT_VERSION-mbstring \  
php$PHP_EXT_VERSION-mysql \  
php$PHP_EXT_VERSION-opcache \  
php$PHP_EXT_VERSION-xml \  
php$PHP_EXT_VERSION-zip \  
php-imagick  
  
# Install Development tools  
RUN apt-get -y install php-pear php$PHP_EXT_VERSION-dev mcrypt
php$PHP_EXT_VERSION-mcrypt  
  
# Expose apache.  
EXPOSE 80 443  
# Update the default apache site with the config we created.  
COPY ./000-default.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Copy php-fpm config  
COPY ./www.conf /etc/php/7.1/fpm/pool.d/www.conf  
  
# Copy server start up scripts  
COPY ./php_entrypoint.sh /opt/php_entrypoint.sh  
  
# Run startup scripts  
RUN chmod 777 /opt/php_entrypoint.sh  
  
ENTRYPOINT ["/opt/php_entrypoint.sh"]  

