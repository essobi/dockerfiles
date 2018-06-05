FROM php:5-apache  
MAINTAINER Quang <quang.astronaut@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo 'mariadb-server-10.0 mysql-server/root_password password p@ssw0rd' |
debconf-set-selections  
RUN echo 'mariadb-server-10.0 mysql-server/root_password_again password
p@ssw0rd' | debconf-set-selections  
RUN apt-get install -y mariadb-server  
  
RUN apt-get install -y php5-mysql  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mysql pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
RUN docker-php-ext-enable gd mysql pdo_mysql  
  
RUN apt-get install -y wget curl git supervisor  
  
COPY conf/php.ini /usr/local/etc/php/  
  
RUN git clone \--depth 1 https://github.com/RandomStorm/DVWA /var/www/html  
  
RUN rm -f /var/www/html/php.ini  
  
RUN chown -R www-data:www-data /var/www/html  
  
COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
EXPOSE 3306  
CMD ["/usr/bin/supervisord"]  

