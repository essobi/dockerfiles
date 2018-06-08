FROM php:5.6-apache  
  
MAINTAINER KikoV <kikov79@gmail.com>  
  
ENV MANTISBT_VERSION 1.3.4  
# Fix sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
COPY docker-entrypoint.sh /entrypoint.sh  
  
RUN a2enmod ssl  
  
RUN apt-get update && apt-get install -y \  
wget \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-configure mysqli && rm -rf /var/lib/apt/lists/*  
  
# Download mantisbt  
RUN cd /var/www/html && \  
wget --quiet --no-cookies
http://sourceforge.net/projects/mantisbt/files/mantis-
stable/${MANTISBT_VERSION}/mantisbt-${MANTISBT_VERSION}.tar.gz/download \  
-O mantisbt-${MANTISBT_VERSION}.tar.gz && \  
tar xvfz mantisbt-${MANTISBT_VERSION}.tar.gz -C /var/www/html --strip-
components=1 && \  
rm mantisbt-${MANTISBT_VERSION}.tar.gz && \  
chown www-data:www-data -R *  
  
EXPOSE 80  
EXPOSE 443  
VOLUME "/var/www/html"  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

