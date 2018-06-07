FROM php:5.6-apache  
  
RUN apt-get update \  
&& apt-get install -y libmcrypt-dev \  
libjpeg62-turbo-dev \  
libpcre3-dev \  
libpng12-dev \  
libfreetype6-dev \  
libxml2-dev \  
libicu-dev \  
mysql-client \  
wget \  
unzip \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install iconv intl mcrypt pdo pdo_mysql mbstring soap gd zip  
  
RUN docker-php-source extract \  
&& if [ -d "/usr/src/php/ext/mysql" ]; then docker-php-ext-install mysql; fi \  
&& if [ -d "/usr/src/php/ext/opcache" ]; then docker-php-ext-install opcache;
fi \  
&& docker-php-source delete  
  
RUN apt-get update \  
&& apt-get install -y git  
  
RUN apt-get update \  
&& apt-get install -y vim nano  
  
RUN apt-get update \  
&& apt-get install -y zip  
  
RUN apt-get update \  
&& apt-get install -y sendmail  
  
# Apache configuration  
RUN a2enmod rewrite  
  
RUN mkdir -p /var/www  
  
COPY /config_files/vhosts/app.conf /etc/apache2/sites-available/  
  
RUN a2ensite app.conf  
RUN chown www-data:www-data -R /var/www  
  
RUN service apache2 restart  

