FROM php:7-fpm  
MAINTAINER Richard Scoop <richard.scoop@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y \  
&& apt-get install -y -qq git libmcrypt-dev libpng12-dev libjpeg-dev libpq-dev
mysql-client curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install mcrypt gd mbstring pdo pdo_mysql zip \  
&& pecl install xdebug \  
&& rm -rf /tmp/pear \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#The following lines allows the first user of the host  
#to remain the owner of the files while they are shared with the container  
#1000 is the uid and gid of the host user, change if yours is not 1000  
RUN usermod -u 1000 www-data && groupmod -g 1000 www-data && usermod -g 1000
www-data && apt-get purge -y --auto-remove && apt-get clean  
  
USER www-data  
  
WORKDIR /var/www  
  

