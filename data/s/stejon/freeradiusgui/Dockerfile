FROM php:5.6-apache  
  
MAINTAINER Sergio Tejón <sergio.tejon@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev  
  
RUN docker-php-ext-install mysql  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
RUN pear install DB-1.8.0 mail  
  
ADD ./html /var/www/html  
  
ADD config.sh /root/  
  
ENV DB_HOST_VALUE=localhost  
ENV DB_PORT_VALUE=3306  
ENV DB_USER_VALUE=radius  
ENV DB_PASS_VALUE=radpass  
ENV DB_NAME_VALUE=radius  
  
EXPOSE 80  
EXPOSE 443  
ADD ./php.ini /usr/local/etc/php/php.ini  
  
WORKDIR /var/www/html  
CMD /root/config.sh ; apachectl -D FOREGROUND  

