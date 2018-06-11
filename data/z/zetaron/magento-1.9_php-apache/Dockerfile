FROM php:5.6-apache  
  
RUN buildDeps=" \  
libpng12-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libxml2-dev \  
freetype* \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure \  
gd --with-png-dir=/usr --with-jpeg-dir=/usr --with-freetype-dir \  
&& docker-php-ext-install \  
gd \  
mbstring \  
mcrypt \  
pdo_mysql \  
soap \  
zip \  
&& apt-get purge -y --auto-remove  
  
RUN a2enmod headers \  
&& a2enmod ssl \  
&& a2enmod rewrite  
  
COPY 001-https.conf /etc/apache2/sites-enabled/001-https.conf  
  
EXPOSE 80 443  

