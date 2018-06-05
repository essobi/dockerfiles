# Copy of its2/backend/Dockerfile  
FROM php:5.6-fpm  
  
RUN apt-get update && apt-get install -y \  
vim \  
libssl-dev \  
wget \  
libcurl4-openssl-dev \  
pkg-config \  
git \  
libicu-dev \  
libxslt-dev \  
graphviz \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
RUN mkdir /application  
WORKDIR /application  
VOLUME /application  
  
RUN usermod -u 1000 www-data && usermod -G staff www-data  
  
RUN pecl install xdebug  
RUN pecl install mongodb  
RUN pecl install mongo  
RUN pecl install zip  
  
RUN docker-php-ext-enable mongodb  
RUN docker-php-ext-enable mongo  
RUN docker-php-ext-enable zip  
RUN docker-php-ext-enable xdebug  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-configure xsl  
RUN docker-php-ext-install -j$(nproc) intl  
RUN docker-php-ext-install xsl  

