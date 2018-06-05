FROM ubuntu:14.04  
MAINTAINER Aloha Lin <knives1003@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main restricted
universe" > /etc/apt/sources.list ;\  
echo "deb http://security.ubuntu.com/ubuntu trusty-security main restricted
universe" >> /etc/apt/sources.list ;\  
apt-get update -q ;\  
apt-get upgrade -y -q ;\  
apt-get dist-upgrade -y -q  
  
RUN apt-get install -y -q php5-dev php5-mcrypt php5-curl php5-pgsql php5-mysql
php5-sqlite php5-mongo php5-memcached php5-xdebug php-apc php5-imagick php5-gd
php5-geoip gcc git libpcre3-dev  
  
RUN git clone \--depth=1 git://github.com/phalcon/cphalcon.git
/usr/local/src/cphalcon  
RUN cd /usr/local/src/cphalcon/build && ./install ;\  
echo "extension=phalcon.so" > /etc/php5/mods-available/phalcon.ini ;\  
php5enmod phalcon  
  
RUN apt-get clean  
  
ENV DEBIAN_FRONTEND dialog  

