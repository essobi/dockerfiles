FROM php:7.0-fpm  
  
RUN apt-get update && apt-get install curl  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
RUN apt-get update  
RUN apt-get install -y nodejs  
RUN node -v  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
libpq-dev \  
libzip-dev \  
libicu-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libwebp-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-webp-dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install pdo \  
&& docker-php-ext-install pdo_pgsql \  
&& docker-php-ext-install pgsql \  
&& docker-php-ext-install intl \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["php-fpm"]  

