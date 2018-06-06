#FROM ubuntu:16.04  
FROM php:5-apache  
#RUN apt-get update && apt-get -y install apache2 libapache2-mod-php php-mysql
supervisor  
RUN apt-get update  
RUN apt-get -y install vim net-tools supervisor libmysqlclient-dev apache2-dev  
RUN apt-get -y install supervisor libmysqlclient-dev apache2-dev  
ADD usr/src /usr/src  
WORKDIR /usr/src/mod_auth_cookie_mysql2_1.0  
RUN make && make install  
RUN apt-get -y remove apache2-dev && apt-get -y autoremove \  
&& apt-get -y install libgd-dev libmcrypt-dev libgd3 libmcrypt4 libpng12-dev
libfreetype6-dev libjpeg62-turbo-dev \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd pdo_mysql mysqli mysql zip  
WORKDIR /  
COPY usr/local/sbin /usr/local/sbin  
EXPOSE 80/tcp 443/tcp  
CMD run.sh  

