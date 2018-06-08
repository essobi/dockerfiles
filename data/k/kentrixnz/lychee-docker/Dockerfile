FROM php:7-apache  
MAINTAINER qhua948@aucklanduni.ac.nz  
  
# Install gd dependencies  
RUN apt-get update && \  
apt-get install -yq git \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libgd-dev  
  
# Config php and modules  
RUN docker-php-source extract \  
docker-php-ext-install -j$(nproc) \  
session \  
mbstring \  
mysqli \  
pdo \  
pdo_mysql \  
json \  
zip \  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install \  
gd \  
exif \  
&& docker-php-source delete  
  
RUN service apache2 start  
RUN a2enmod php7 rewrite  
RUN service apache2 restart  
  
# Install Lychee  
WORKDIR /var/www  
RUN git clone https://github.com/electerious/Lychee.git html  
RUN chown -R www-data:www-data /var/www/html  
RUN chmod -R 770 /var/www/html  
RUN chmod -R 777 /var/www/html/uploads/  
RUN chmod -R 777 /var/www/html/data/  
RUN mkdir -p /var/lycheeimport/  
RUN chown -R www-data:www-data /var/lycheeimport/  
RUN chmod -R 777 /var/lycheeimport/  
  
# Expose port(s)  
EXPOSE 80  
RUN apt-get remove --purge -y git  
  
# Expose volumes  
WORKDIR /  
VOLUME /var/www/html/uploads  
VOLUME /var/www/html/data  
  
COPY ./docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
COPY php.ini /usr/local/etc/php/  
CMD ["/docker-entrypoint.sh"]  

