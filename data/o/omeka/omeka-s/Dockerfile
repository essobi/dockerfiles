FROM php:7.1-apache  
  
RUN a2enmod rewrite  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -qq update && apt-get -qq -y --no-install-recommends install \  
curl \  
unzip \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libjpeg-dev \  
libmemcached-dev \  
zlib1g-dev \  
imagemagick  
  
# install the PHP extensions we need  
RUN docker-php-ext-install -j$(nproc) iconv mcrypt \  
pdo pdo_mysql mysqli gd  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
  
RUN curl -J -L -s -k \  
'https://github.com/omeka/omeka-s/releases/download/v1.0.0-beta3/omeka-s.zip'
\  
-o /var/www/omeka-s.zip \  
&& unzip -q /var/www/omeka-s.zip -d /var/www/ \  
&& rm /var/www/omeka-s.zip \  
&& rm -rf /var/www/html \  
&& mv /var/www/omeka-s /var/www/html \  
&& chown -R www-data:www-data /var/www/html  
  
COPY ./database.ini /var/www/html/config/database.ini  
COPY ./imagemagick-policy.xml /etc/ImageMagick/policy.xml  
COPY ./.htaccess /var/www/html/.htaccess  
  
VOLUME /var/www/html  
  
CMD ["apache2-foreground"]  

