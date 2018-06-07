# Node.js + Socket.io + PHP 56 + composer  
FROM phusion/baseimage:0.9.17  
MAINTAINER Doitmagic <razvan@doitmagic.com>  
  
ENV COMPOSER_VERSION=1.1.2  
RUN mkdir -p /var/www  
RUN mkdir -p /var/script  
RUN mkdir -p /node_modules  
  
#Install php + composer  
RUN apt-get update && apt-get install -y --force-yes php5 php5-fpm php5-cli
php5-mysql php5-mcrypt php5-gd php5-curl php5-intl  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
#install node 6.X + socket.io  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
  
RUN apt-get update && apt-get install -y nodejs  
RUN apt-get install -y python build-essential  
  
VOLUME [/var/www,/var/script,/node_modules]  
  
WORKDIR /var/script  
  
EXPOSE 3500/tcp 6379  
CMD "/bin/sh" "-c" "node index.js"  

