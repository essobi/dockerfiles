FROM php:5.6-fpm  
  
MAINTAINER Thomas Sieffert <thomas.sieffert@devitek.fr>  
  
RUN apt-get update && apt-get install -y \  
libz-dev \  
libmemcached-dev \  
libcurl4-openssl-dev \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& pecl install memcached \  
&& docker-php-ext-install pdo_mysql gettext zip  
  
RUN apt-get update && apt-get install -y \  
zlib1g-dev \  
libicu-dev \  
g++ \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install intl  
  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install -j$(nproc) mcrypt  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get install -y nodejs \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y \  
git \  
wget \  
vim \  
zip \  
unzip \  
bzip2 \  
libfontconfig \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8000  
  
WORKDIR /opt  
  
CMD ["bash"]  

