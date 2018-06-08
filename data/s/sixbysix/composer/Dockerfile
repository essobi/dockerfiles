FROM php:7.0  
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
libicu-dev \  
libmcrypt-dev \  
libxslt-dev \  
libzip-dev \  
&& docker-php-ext-install -j$(nproc) intl mcrypt xsl zip bcmath soap pdo_mysql
\  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /app  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
ENV COMPOSER_VERSION 1.6.4  
  
CMD ["composer"]  

