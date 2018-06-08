FROM php:5.5-apache  
  
ENV SIREMIS_VERSION=4.2.0  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
curl libcurl4-gnutls-dev \  
make \  
&& docker-php-ext-install -j$(nproc) pdo iconv mcrypt curl mysql mysqli
pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN mkdir -p /var/www  
RUN cd /var/www && curl -o siremis.tgz
"http://siremis.asipto.com/pub/downloads/siremis/siremis-${SIREMIS_VERSION}.tgz"
\  
&& tar -zxf siremis.tgz && rm siremis.tgz && ln -s
/var/www/siremis-${SIREMIS_VERSION} /var/www/siremis  
  
ADD src/sites-available /etc/apache2/sites-available  
RUN ln -s /etc/apache2/sites-available/001-siremis.conf /etc/apache2/sites-
enabled/001-siremis.conf  
  
WORKDIR /var/www/siremis  

