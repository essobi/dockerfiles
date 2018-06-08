FROM php:apache  
  
MAINTAINER Rosiney Gomes Pereira <rosiney.gp@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y wget libtidy-dev libcurl4-openssl-dev sqlite3
libsqlite3-dev gettext gettext libfreetype6-dev libjpeg62-turbo-dev libmcrypt-
dev libpng12-dev zip unzip  
  
RUN docker-php-ext-install iconv mcrypt pdo_sqlite curl json tidy gettext gd
mbstring zip pdo pdo_mysql  
  
RUN wget https://github.com/wallabag/wallabag/archive/2.0.2.tar.gz  
RUN tar -zxvf 2.0.2.tar.gz  
RUN cp -rf wallabag-2.0.2/* /var/www/html  
RUN rm -rf wallabag-2.0.2  
RUN cd /var/www/html && curl -s http://getcomposer.org/installer | php && php
composer.phar install  
RUN chown -R www-data:www-data /var/www/html  
  
VOLUME /var/www/html  
EXPOSE 80  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

