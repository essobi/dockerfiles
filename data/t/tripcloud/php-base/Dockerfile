FROM php:7.1  
RUN apt-get update && apt-get install -y unzip git mercurial libmcrypt-dev
libxml2-dev libssh2-1-dev libpng12-dev libssl-dev libicu-dev  
  
RUN docker-php-ext-install gd soap sockets  
  
RUN docker-php-ext-install -j$(nproc) mcrypt intl  
  
RUN pecl install mongodb ssh2-1.0  
  
RUN docker-php-ext-enable mongodb ssh2  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

