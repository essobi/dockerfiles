# Version 1.0.0  
# cyan.img.Lamp  
#========== Basic Image ==========  
From php:5.4-apache  
MAINTAINER "DreamInSun"  
#========== Environment ==========  
ENV APACHE_DOC /var/www/html/  
  
#========== Configuration ==========  
#========== Install Framework ==========  
COPY config/php.ini /usr/local/etc/php/  
RUN apt-get update  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev  
RUN docker-php-ext-install iconv mcrypt  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && docker-php-ext-install gd  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install mysql  
#RUN docker-php-ext-install xdebug  
#========== Install Application ==========  
#========== Expose Ports ==========  
#========= RUN ==========  
#ADD shell /shell  
#RUN chmod a+x /shell/*  
#========= Start Service ==========  
#ENTRYPOINT ["/shell/docker-entrypoint.sh"]  
CMD [ "apache2-foreground" ]

