FROM ubuntu:16.04  
MAINTAINER Tom Janke <info@tomjanke.de>  
  
RUN apt-get clean  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >>
/etc/apt/sources.list  
RUN echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu xenial main" >>
/etc/apt/sources.list  
RUN sed -i 's/^#\s*\\(deb.*main restricted\\)$/\1/g' /etc/apt/sources.list  
RUN sed -i 's/^#\s*\\(deb.*universe\\)$/\1/g' /etc/apt/sources.list  
RUN sed -i 's/^#\s*\\(deb.*multiverse\\)$/\1/g' /etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get -y install locales  
RUN locale-gen de_DE.UTF-8  
  
ENV DEBIAN_FRONTEND="noninteractive" \  
LANG="de_DE.UTF-8" \  
LANGUAGE="de_DE:de" \  
LC_ALL="de_DE.UTF-8"  
RUN rm -f /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Berlin /etc/localtime  
RUN apt-get clean  
RUN apt-get update  
RUN apt-get install -y \  
apache2 \  
libapache2-mod-php7.1 \  
php7.1 \  
php7.1-cli \  
php7.1-apcu \  
php7.1-gd \  
php7.1-json \  
php7.1-mbstring \  
php7.1-mysql \  
php7.1-opcache \  
php7.1-xml \  
php7.1-zip \  
php7.1-xdebug \  
php7.1-intl \  
composer \  
nodejs \  
npm  
  
COPY 000-default.txt /etc/apache2/sites-enabled/000-default.conf  
COPY php.txt /etc/php/7.1/apache2/php.ini  
  
RUN npm install -g uglify-js less uglifycss  
RUN ln -s /usr/local/lib/node_modules/less /usr/local/bin/less  
RUN ln -s /usr/bin/nodejs /usr/local/bin/node  
RUN a2enmod rewrite  
RUN apt-get clean  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y dist-upgrade  
RUN echo "#!/bin/bash" > /usr/sbin/init  
RUN echo "rm -f /run/apache2/apache2.pid 2> /dev/null" >> /usr/sbin/init  
RUN echo "source /etc/apache2/envvars" >> /usr/sbin/init  
RUN echo "exec /usr/sbin/apache2 -D FOREGROUND" >> /usr/sbin/init  
RUN chmod +x /usr/sbin/init  
  
EXPOSE 80  
EXPOSE 443  
VOLUME /var/www/html  
  
CMD ["/usr/sbin/init"]

