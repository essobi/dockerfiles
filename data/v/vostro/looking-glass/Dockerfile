FROM php:apache  
MAINTAINER Guillaume Mazoyer <gmazoyer@gravitons.in>  
RUN apt-get update \  
&& apt-get -y install bash ssh libmcrypt-dev openssl libsodium-dev libgmp-dev
libgmp3-dev \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& docker-php-ext-install -j$(nproc) mcrypt gmp \  
&& pecl install libsodium \  
&& docker-php-ext-enable libsodium \  
&& mkdir -p /var/log/ \  
&& touch /var/log/looking-glass.log \  
&& chown www-data /var/log/looking-glass.log  
  
WORKDIR /var/www/html/  
ADD ./ ./  
RUN chown -R www-data /var/www/html  

