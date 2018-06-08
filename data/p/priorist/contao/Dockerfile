FROM php:5-apache  
  
MAINTAINER priorist <contact@priorist.com>  
  
RUN apt-get update && \  
apt-get install -y wget zip libfreetype6-dev libjpeg62-turbo-dev libpng12-dev
zlib1g-dev libicu-dev libxml2-dev g++ && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) mysqli gd intl soap && \  
curl -s https://api.github.com/repos/contao/core/releases/latest | grep
browser_download_url | grep zip | xargs | cut -c 23\- | xargs wget && \  
unzip *.zip && \  
rm *.zip && \  
/bin/bash -c "shopt -s dotglob && mv contao-*/* . && chown -R www-data:www-
data *" && \  
rm -r contao-* && \  
mv .htaccess.default .htaccess && \  
apt-get remove -y wget zip g++ && \  
rm -rf /var/lib/apt/lists/*  

