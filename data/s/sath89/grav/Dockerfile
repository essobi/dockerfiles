FROM php:7-apache  
  
MAINTAINER sath891@gmail.com  
  
RUN apt-get update && apt-get install -y git libzip-dev libfreetype6-dev
libjpeg62-turbo-dev libmcrypt-dev libpng12-dev libssl-dev libxml2-dev
libcurl4-gnutls-dev && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd zip curl mbstring xml && \  
apt-get purge -y libzip-dev libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev libssl-dev libxml2-dev libcurl4-gnutls-dev && \  
apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
COPY etc /etc  
  
RUN a2enmod rewrite && a2dissite 000-default && a2ensite grav  
  
ENV BRANCH develop  
  
WORKDIR /var/www/grav  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]

