FROM debian:jessie  
  
MAINTAINER "Braydee Johnson" <braydee@braydeejohnson.com>  
  
RUN \  
apt-get update && \  
apt-get install -y \  
curl \  
wget \  
git \  
vim  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
wget -O- http://www.dotdeb.org/dotdeb.gpg | apt-key add -  
  
RUN \  
apt-get update && \  
apt-get install -y \  
php7.0-bcmath \  
php7.0-cgi \  
php7.0-cli \  
php7.0-curl \  
php7.0-gd \  
php7.0-imagick \  
php7.0-imap \  
php7.0-json \  
php7.0-ldap \  
php7.0-mbstring \  
php7.0-mcrypt \  
php7.0-memcached \  
php7.0-mongodb \  
php7.0-msgpack \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-redis \  
php7.0-sqlite3 \  
php7.0-tidy \  
php7.0-xdebug \  
php7.0-xmlrpc \  
php7.0-xsl \  
php7.0-zip  
  
RUN apt-get install -y \  
php-pear \  
php7.0-dev \  
libsasl2-dev \  
libcurl3-openssl-dev  
  
RUN pecl install mongodb  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
composer global require "laravel/installer" && \  
composer global require "laravel/envoy=~1.0"  
  
ENV PATH "/root/.composer/vendor/bin:$PATH"  
  
ENTRYPOINT ["php"]  
CMD ["--help"]

