FROM php:fpm  
  
RUN apt-get update  
RUN apt-get install -y libssl-dev libpng-dev libmagickwand-dev libgmp-dev
zlib1g-dev libicu-dev g++ git-all  
  
RUN docker-php-ext-configure intl  
  
RUN docker-php-ext-install iconv mbstring exif zip gd intl pcntl  
  
RUN pecl install mongodb  
RUN pecl install imagick  
RUN pecl install apcu  
  
RUN docker-php-ext-enable mongodb  
RUN docker-php-ext-enable imagick  
RUN docker-php-ext-enable apcu  
  
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h  
RUN docker-php-ext-configure gmp --with-gmp=/usr/include/x86_64-linux-gnu  
RUN docker-php-ext-install gmp  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer

