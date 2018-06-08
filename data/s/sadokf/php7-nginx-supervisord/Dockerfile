FROM php:7.1-fpm  
  
MAINTAINER sadoknet@gmail.com  
  
RUN \  
apt-get -y update && \  
apt-get -y install \  
curl vim wget git build-essential make gcc nasm mlocate apt-transport-https\  
nginx supervisor  
  
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg && \  
echo "deb https://packages.sury.org/php/ jessie main" >
/etc/apt/sources.list.d/php.list  
  
# Install PHP7 dependencies  
RUN apt-get update -yqq \  
&& apt-get -y install libsqlite3-dev libcurl4-openssl-dev libpng12-dev libicu-
dev libc-client-dev libmcrypt-dev libxml2-dev libxslt-dev libssl-dev
libbz2-dev libfreetype6-dev libjpeg62-turbo-dev  
  
# Install PHP7 extensions  
RUN docker-php-ext-install pdo_mysql \  
pdo_sqlite opcache json calendar gd \  
bcmath xml zip bz2 mbstring mcrypt curl sockets  
  
# Install PECL extensions  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& docker-php-ext-install intl  
  
COPY resources/etc/ /etc/  
  
#install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
ADD . /var/www  
WORKDIR /var/www  
  
RUN usermod -u 1000 www-data  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]

