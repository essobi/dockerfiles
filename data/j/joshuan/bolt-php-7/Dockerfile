FROM php:7.0-fpm  
  
RUN apt-get update -y  
  
RUN apt-get install -y --no-install-recommends apt-utils  
RUN docker-php-ext-install pdo_mysql  
  
RUN apt-get install -y --no-install-recommends libpng-dev libfreetype6-dev
libjpeg62-turbo-dev libpng12-dev libxpm-dev libvpx-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/lib/x86_64-linux-gnu/
--with-jpeg-dir=/usr/lib/x86_64-linux-gnu/ --with-xpm-
dir=/usr/lib/x86_64-linux-gnu/ --with-vpx-dir=/usr/lib/x86_64-linux-gnu/  
RUN docker-php-ext-install gd  
  
RUN apt-get install -y --no-install-recommends libgmp-dev libgmp3-dev  
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h  
RUN docker-php-ext-install gmp  
  
RUN docker-php-ext-install json  
  
RUN docker-php-ext-install mbstring  
  
RUN docker-php-ext-install posix  
  
RUN apt-get install -y --no-install-recommends libxml2-dev  
RUN docker-php-ext-install xml  
  
RUN docker-php-ext-install fileinfo  
  
RUN docker-php-ext-install exif  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php  
RUN rm composer-setup.php  
RUN mv composer.phar /usr/local/bin/composer.phar  
  
RUN apt-get install -y git  
  
RUN rm -rf /var/lib/apt/lists/*  

