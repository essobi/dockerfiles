FROM php:7.1-fpm  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y \  
libpng12-dev libfreetype6-dev libjpeg62-turbo-dev \  
libjpeg-dev libpq-dev zip unzip wget git imagemagick \  
zlib1g-dev libicu-dev g++ libmagickwand-dev  
  
RUN wget -O - https://packagecloud.io/gpg.key | apt-key add -  
  
RUN echo "deb http://packages.blackfire.io/debian any main" | tee
/etc/apt/sources.list.d/blackfire.list  
  
RUN apt-get update && apt-get install -y \  
blackfire-agent blackfire-php  
  
RUN docker-php-ext-install mysqli gd pdo_mysql pdo_pgsql intl  
  
RUN pecl install imagick  
  
RUN docker-php-ext-enable imagick imagick.so  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
  
#Install postgres  
ADD postgres.sql /temp/postgres.sql  
ADD postgres-install.sh /temp/postgres-install.sh  
RUN /temp/postgres-install.sh  
ADD postgres-fulltextsearch.sql /temp/postgres-fulltextsearch.sql  
ADD postgres-fulltextsearch.sh /temp/postgres-fulltextsearch.sh  
RUN /temp/postgres-fulltextsearch.sh  
  
ADD composer_installer.sh /temp/composer_installer.sh  
  
RUN /temp/composer_installer.sh  
  

