FROM php:5.4-apache  
MAINTAINER Subak Systems <info@subak.jp>  
  
RUN a2enmod rewrite  
  
RUN apt-get update && apt-get install -y libjpeg62-turbo-dev libpng12-dev &&
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ && \  
docker-php-ext-install gd  
  
RUN docker-php-ext-configure mbstring --enable-mbstring && \  
docker-php-ext-install mbstring  
  
RUN docker-php-ext-configure mysql --with-mysql && \  
docker-php-ext-install mysql  
  
RUN apt-get update && apt-get install -y ssmtp && rm -rf /var/lib/apt/lists/*
&& \  
echo 'sendmail_path = /usr/sbin/ssmtp -t' >
/usr/local/etc/php/conf.d/ssmtp.ini  
  
RUN echo 'upload_max_filesize = 8M' > /usr/local/etc/php/conf.d/php.ini  

