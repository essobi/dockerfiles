FROM php:apache  
  
RUN apt-get update &&\  
apt-get install -y --no-install-recommends \  
wget curl unzip \  
libxml2-dev libfreetype6-dev librecode-dev librecode0 \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
graphicsmagick && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) mysqli soap gd zip opcache mcrypt xmlrpc  
  
RUN apt-get clean && \  
apt-get -y purge \  
libxml2-dev libfreetype6-dev librecode-dev librecode0 \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev && \  
rm -rf /var/lib/apt/lists/* /usr/src/* /tmp/*  
  
RUN { \  
echo 'ServerTokens Prod'; \  
echo 'ServerSignature Off'; \  
} >> /etc/apache2/apache2.conf  
  
RUN a2enmod rewrite  
  
RUN echo 'date.timezone= "Europe/Berlin"' > /usr/local/etc/php/conf.d/php.ini  
RUN echo 'expose_php = off' >> /usr/local/etc/php/conf.d/php.ini  
  
VOLUME /var/www/html  
WORKDIR /var/www/html  
  
CMD ["apache2-foreground"]

