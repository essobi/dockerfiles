# Set the base image  
FROM php:7.2-fpm-stretch  
# Dockerfile author / maintainer  
MAINTAINER Charlotte Bone <charlotte.b@mmtdigital.co.uk>  
  
RUN apt-get update && apt-get install -y unzip git curl gnupg2 \  
&& curl -sL https://deb.nodesource.com/setup_9.x | bash - \  
&& apt-get -y install nodejs fontforge ttfautohint libpng-dev \  
&& docker-php-ext-install gd \  
&& npm install -g npm \  
&& npm install -g grunt-cli \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  

