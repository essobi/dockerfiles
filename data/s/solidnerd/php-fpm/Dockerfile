FROM php:5.6-fpm  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
libgmp3-dev \  
g++ \  
libicu-dev \  
libbz2-dev \  
libcurl4-openssl-dev \  
libpq-dev \  
libsqlite3-dev \  
libxml2-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install ctype \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install dom \  
&& docker-php-ext-install json \  
&& docker-php-ext-install posix \  
&& docker-php-ext-install pdo_sqlite \  
&& docker-php-ext-install mysql \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install pgsql \  
&& docker-php-ext-install pdo_pgsql \  
&& docker-php-ext-install curl \  
&& docker-php-ext-install fileinfo \  
&& docker-php-ext-install bz2 \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install exif \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& docker-php-ext-install gmp  
CMD ["php-fpm"]  

