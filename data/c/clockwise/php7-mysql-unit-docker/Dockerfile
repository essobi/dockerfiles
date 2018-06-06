FROM php:latest  
  
MAINTAINER Dmitry Boyko <dmitry@thebodva.com>  
  
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');"  
RUN php /tmp/composer-setup.php --no-ansi \--install-dir=/usr/local/bin
\--filename=composer && \  
rm -rf /tmp/composer-setup.php  
  
RUN apt-get update && \  
apt-get install -y git unzip  
  
RUN apt-get update && \  
apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libsqlite3-dev \  
libcurl4-gnutls-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt gd pdo_mysql pcntl
pdo_sqlite zip curl bcmath opcache mbstring \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-enable iconv mcrypt gd pdo_mysql pcntl pdo_sqlite zip curl
bcmath opcache mbstring \  
&& apt-get autoremove -y  
  
RUN apt-get update && \  
export DEBIAN_FRONTEND="noninteractive" && \  
apt-get install -y mysql-server-5.5 && \  
service mysql start && \  
service mysql status  
  
RUN apt-get update && \  
apt-get install -y redis-server  
  
EXPOSE 3306 6379

