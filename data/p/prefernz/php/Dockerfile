# Extend from current stable php apache  
FROM php:7.2-apache  
  
# OS packages  
RUN apt-get -y update && apt-get install -y \  
zlib1g-dev \  
libicu-dev \  
libpng-dev \  
libjpeg-dev \  
libwebp-dev \  
zip \  
unzip \  
curl \  
git \  
ssh \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
# PHP Extensions  
RUN docker-php-ext-configure intl \  
&& docker-php-ext-configure gd --with-png-dir=/usr/lib --with-jpeg-
dir=/usr/lib --with-webp-dir=/usr/lib  
RUN docker-php-ext-install \  
pdo_mysql \  
mysqli \  
intl \  
gd \  
bcmath  
  
# Composer binary  
RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer
--install-dir=/usr/local/bin  
RUN composer -V  
  
# PHP config  
COPY ["./conf/php/", "/usr/local/etc/php/"]  
  
# Apache Configuration  
COPY ["./conf/apache2/docker.conf", "/etc/apache2/sites-
available/000-default.conf"]  
COPY ["./conf/apache2/docker-ssl.conf", "/etc/apache2/sites-available/default-
ssl.conf"]  
RUN a2enmod headers rewrite  

