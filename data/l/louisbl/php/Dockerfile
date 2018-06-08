FROM php:7.1-cli  
MAINTAINER louisbl <louisbl@beltramo.me>  
  
RUN apt-get update && apt-get install -y \  
g++ \  
git \  
imagemagick \  
libbz2-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq-dev \  
libxslt1-dev \  
libzip-dev \  
mysql-client \  
openssh-client \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /usr/include/freetype2/freetype && ln -s
/usr/include/freetype2/freetype.h /usr/include/freetype2/freetype/freetype.h  
  
RUN docker-php-ext-configure gd --with-jpeg-dir --with-freetype-dir --enable-
gd-native-ttf \  
&& docker-php-ext-install -j$(nproc) \  
bz2 \  
gd \  
exif \  
intl \  
mbstring \  
mcrypt \  
mysqli \  
pdo_mysql \  
zip  
  
RUN echo "date.timezone = \"Europe/Paris\"" >
/usr/local/etc/php/conf.d/timezone.ini  
RUN echo "memory_limit=-1" > /usr/local/etc/php/conf.d/memory-limit.ini  
RUN echo "zend.enable_gc=0" > /usr/local/etc/php/conf.d/disable-gc.ini  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

