FROM ubuntu:14.04  
MAINTAINER Vladimir Metelitsa <me@greencat.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -q  
RUN apt-get upgrade -y -q  
  
RUN apt-get install -y -q -f php5-dev php5-mcrypt php5-mbstring php5-curl
php5-mongo php5-json php5-memcached php5-xdebug php5-gd php5-geoip libtool git
libpcre3-dev curl  
  
ENV COMPOSER_HOME /root/composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN /usr/local/bin/composer global require "codeception/codeception:*"  
  
RUN git clone \--depth=1 git://github.com/phalcon/cphalcon.git
/usr/local/src/cphalcon  
RUN cd /usr/local/src/cphalcon/build && ./install ;\  
echo "extension=phalcon.so" > /etc/php5/mods-available/phalcon.ini ;\  
php5enmod phalcon  
  
RUN apt-get clean  
  
ENV DEBIAN_FRONTEND dialog  

