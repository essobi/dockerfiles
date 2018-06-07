FROM php:apache  
  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
&& docker-php-ext-install -j$(nproc) mcrypt pdo_mysql \  
&& apt-get remove -y libmcrypt-dev \  
&& rm -rf /var/lib/apt/lists/*  

