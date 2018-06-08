FROM php:apache  
  
EXPOSE 80  
RUN apt-get update && apt-get install -y \  
cron \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install mysqli gd zip  
  
COPY src/ /var/www/html  
  
RUN chown -R www-data.www-data /var/www/html  
  
COPY init.sh /init.sh  
  
ENTRYPOINT ["/init.sh"]  

