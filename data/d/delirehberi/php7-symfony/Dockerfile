FROM php:7.1-fpm  
RUN apt-get update  
RUN apt-get install -y libfreetype6-dev  
RUN apt-get install -y libjpeg62-turbo-dev  
RUN apt-get install -y libmcrypt-dev  
RUN apt-get install -y libpng12-dev  
RUN apt-get install -y zlib1g-dev  
RUN apt-get install -y libicu-dev  
RUN apt-get install -y libpq-dev  
RUN apt-get install -y g++  
RUN apt-get install -y libzip-dev  
RUN docker-php-ext-install -j$(nproc) iconv mcrypt  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install -j$(nproc) gd  
RUN docker-php-ext-install -j$(nproc) pdo  
RUN docker-php-ext-install -j$(nproc) mbstring  
RUN docker-php-ext-install -j$(nproc) exif  
RUN docker-php-ext-configure intl  
RUN docker-php-ext-configure pdo_pgsql  
RUN docker-php-ext-install -j$(nproc) intl  
RUN docker-php-ext-install -j$(nproc) pdo_mysql  
RUN docker-php-ext-install -j$(nproc) pdo_pgsql  
RUN docker-php-ext-install -j$(nproc) mysqli  
RUN pecl install zip  
RUN docker-php-ext-enable zip  
RUN apt-get install -y git  
WORKDIR "/tmp"  
  
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-
setup.php  
RUN php composer-setup.php --install-dir=/bin --filename=composer  
RUN php -r "unlink('composer-setup.php');"  
  
WORKDIR "/var/www"  
RUN usermod -u 1000 www-data  
  
CMD ["php-fpm"]  

