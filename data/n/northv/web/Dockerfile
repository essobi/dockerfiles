FROM php:5.6-apache  
  
RUN a2enmod rewrite  
RUN a2enmod remoteip && echo "RemoteIPHeader X-Real-IP" > /etc/apache2/mods-
enabled/remoteip.conf  
  
# install the PHP extensions we need  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install mysql  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install exif  
RUN apt-get update && apt-get install -y --auto-remove \  
libxslt1-dev \  
libjpeg-dev \  
libpng12-dev \  
php5-imagick \  
libimage-exiftool-perl \  
&& docker-php-ext-install xsl \  
&& docker-php-ext-configure gd --with-jpeg-dir=/usr/local \  
&& docker-php-ext-install gd \  
&& cp /usr/lib/php5/20131226/imagick.so /usr/local/lib/php/extensions/no-
debug-non-zts-20131226/ \  
&& cp /etc/php5/mods-available/imagick.ini /usr/local/etc/php/conf.d/ \  
&& apt-get autoclean && rm -rf /var/lib/apt/lists/*  
  
COPY sendmail /bin/sendmail  
RUN chmod +x /bin/sendmail  
  
COPY apache2.conf /etc/apache2/  
COPY php.ini /usr/local/etc/php/  
COPY apache2/sites /etc/apache2/sites  
  
RUN mkdir -p /var/www/html/default/docs  
RUN mkdir /var/www/logs && chown 33:33 /var/www/logs  
VOLUME /var/www/logs  

