# Akeneo Web  
FROM debian:jessie  
MAINTAINER mauriau <maxime.auriaugmail.com>  
  
# Base + Akeneo requirements  
RUN apt-get update \  
&& apt-get install --no-install-recommends --yes \  
ca-certificates \  
openssh-client \  
curl \  
nano \  
git \  
php5 \  
php5-cli \  
php5-curl \  
php5-gd \  
php5-intl \  
php5-mysqlnd \  
php5-mcrypt \  
php5-apcu \  
libicu-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
&& apt-get clean \\*  
  
RUN rm /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime  
RUN "date"  
  
# Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin  
RUN composer global require "hirak/prestissimo:^0.3"  
# PHP  
COPY ./cli-php.ini /etc/php5/cli/php.ini  
  
# Clean  
RUN rm -rf /tmp/* /var/tmp/*  
  
RUN usermod -u 1000 www-data  
  
WORKDIR /var/www/akaneo  

