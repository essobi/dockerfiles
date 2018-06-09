FROM php:7-fpm  
  
COPY php-timezone.ini /usr/local/etc/php/conf.d/timezone.ini  
  
RUN apt-get update -q \  
&& apt-get install -y libfreetype6 libfreetype6-dev libjpeg62-turbo
libjpeg62-turbo-dev libpng12-0 libpng12-dev \  
&& docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& pecl install redis && docker-php-ext-enable redis \  
&& apt-get install -y libicu52 libicu-dev && docker-php-ext-install -j$(nproc)
intl \  
&& apt-get install -y libcurl3 libcurl4-openssl-dev && docker-php-ext-install
-j$(nproc) curl \  
&& docker-php-ext-install -j$(nproc) pdo pdo_mysql opcache mbstring bcmath
exif \  
&& pecl clear-cache && apt-get remove -y \--auto-remove libfreetype6-dev
libjpeg62-turbo-dev libpng12-dev libicu-dev libcurl4-openssl-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY php-memory.ini /usr/local/etc/php/conf.d/memory.ini  
  

