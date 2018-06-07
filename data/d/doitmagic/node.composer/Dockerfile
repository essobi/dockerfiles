# Node.js + Socket.io + PHP 56 + composer  
FROM phusion/baseimage:0.9.17  
MAINTAINER Doitmagic <razvan@doitmagic.com>  
  
ENV COMPOSER_VERSION=1.1.2  
RUN mkdir -p /var/www  
RUN mkdir -p /var/script  
  
#Install php + composer  
RUN apt-get update && apt-get install -y --force-yes php5 php5-fpm php5-cli
php5-mysql php5-mcrypt php5-gd php5-curl php5-intl  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
#install node + socket.io  
RUN apt-get update && apt-get install -y nodejs  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN apt-get install -y npm  
RUN /usr/bin/npm install express && /usr/bin/npm install socket.io &&
/usr/bin/npm install redis && /usr/bin/npm install ioredis && /usr/bin/npm
install redis-notifier && /usr/bin/npm install request && /usr/bin/npm install
gulp && /usr/bin/npm install laravel-elixir && /usr/bin/npm install bower &&
/usr/bin/npm install gulp-htmlmin  
  
VOLUME [/var/www,/var/script]  
  
WORKDIR /var/script  
  
EXPOSE 3500/tcp 6379  
CMD "/bin/sh" "-c" "node index.js"  
  

