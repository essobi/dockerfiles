FROM php:7-apache  
MAINTAINER Virgilio Missão Neto <virgilio.missao.neto@gmail.com>  
  
RUN curl -fsSL
'https://download.moodle.org/download.php/direct/stable32/moodle-3.2.tgz' -o
moodle.tgz \  
&& mkdir -p moodle \  
&& tar -xf moodle.tgz -C moodle --strip-components=1 \  
&& mv moodle/* /var/www/html \  
&& rm moodle.tgz \  
&& rm -rf moodle  
  
RUN apt-get update  
RUN apt-get install -y php5-mysql libfreetype6-dev libjpeg62-turbo-dev
libmcrypt-dev libpng12-dev php5-gd php5-curl php5-intl php5-xmlrpc zlib1g-dev
libicu-dev g++ libxml2-dev  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-configure intl  
  
RUN docker-php-ext-install -j$(nproc) iconv mcrypt mysqli gd intl xmlrpc zip  
  
RUN mkdir -p /var/www/moodledata  
  
VOLUME /var/www/html  
VOLUME /var/www/moodledata  
  
EXPOSE 80  
CMD ["apache2-foreground"]  

