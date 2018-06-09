FROM debian:9.1  
MAINTAINER Olivier RICARD <olivier.docker@talkspirit.com>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install wget zsh curl vim zsh git re2c
libcurl4-openssl-dev pkg-config libssl-dev -y  
  
## Basic Requirements  
RUN apt-get -y install php7.0-dev php7.0-cli php7.0-curl php7.0-gd php7.0-intl
php7.0-redis php7.0-mongodb php7.0-apcu php7.0-fpm php7.0-dom php7.0-mbstring
php7.0-mcrypt  
  
## build package  
RUN apt-get install -y build-essential debhelper devscripts sudo  
  
# Time Zone  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
/etc/php/7.0/cli/conf.d/date_timezone.ini  
  
RUN cd /etc/php/7.0/mods-available/;echo "xdebug.max_nesting_level = 200" >>
xdebug.ini  
##  
## php-fpm config  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g"
/etc/php/7.0/fpm/php.ini  
RUN sed -i -e "s/listen = \/run\/php\/php7.0-fpm.sock/;listen =
\/run\/php\/php7.0-fpm.sock\nlisten = 0:9000/g"
/etc/php/7.0/fpm/pool.d/www.conf  
##  
## cli config  
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/7.0/cli/php.ini  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

