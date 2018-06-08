FROM phusion/baseimage:0.9.18  
MAINTAINER Asokani "https://github.com/asokani"  
RUN apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold"  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get -y install zip git wget curl joe mysql-client php5-cli php5-mysql
\  
php5-gd php5-imagick php5-tidy busybox openssl mc libmcrypt-dev \  
libmysqlclient-dev graphicsmagick-libmagick-dev-compat libcurl4-openssl-dev
libonig-dev \  
build-essential python-software-properties \  
libssl-dev nodejs  
  
# users acme 1000, www-manage 1001, www-user 1002  
RUN adduser --disabled-password --gecos "" acme && \  
adduser --disabled-password --gecos "" www-manage && \  
adduser --disabled-password --gecos "" www-user && \  
usermod -a -G www-user www-manage  
  
CMD ["/sbin/my_init"]  
  
# TODO RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

