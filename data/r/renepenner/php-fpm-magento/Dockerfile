FROM php:5.6-fpm  
  
RUN apt-get update && \  
apt-get install -y \  
libpng12-dev \  
libjpeg-dev \  
libmcrypt-dev \  
libxml2-dev \  
freetype* \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-configure \  
gd --with-png-dir=/usr --with-jpeg-dir=/usr && \  
\  
docker-php-ext-install \  
gd \  
mbstring \  
mcrypt \  
mysqli \  
opcache \  
pdo \  
pdo_mysql \  
soap \  
zip  
  
RUN apt-get update -qy && apt-get install -qy git-core  

