FROM php:7.0-fpm  
  
COPY files/ioncube_loader_lin_7.0.so /opt/ioncube/  
COPY files/00-ioncube.ini /usr/local/etc/php/conf.d/  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libxml2-dev \  
libc-client-dev \  
libkrb5-dev \  
&& docker-php-ext-install -j$(nproc) pdo_mysql \  
&& docker-php-ext-install -j$(nproc) zip \  
&& docker-php-ext-install -j$(nproc) soap \  
&& docker-php-ext-install -j$(nproc) xmlrpc \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-install imap  
  
RUN echo '[PHP]' > /usr/local/etc/php/php.ini  
RUN echo 'date.timezone = "Europe/Madrid"' >> /usr/local/etc/php/php.ini  
  
EXPOSE 9000  

