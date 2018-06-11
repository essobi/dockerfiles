FROM php:7.1  
MAINTAINER TruckersMP Team  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
libmcrypt-dev \  
openssh-client \  
rsync \  
libicu-dev  
RUN docker-php-ext-install -j$(nproc) iconv mcrypt opcache zip mysqli pdo
pdo_mysql mbstring intl  
RUN docker-php-ext-configure gd \--with-freetype-dir=/usr/include/ \--with-
jpeg-dir=/usr/include/  
RUN docker-php-ext-install -j$(nproc) gd  
  
RUN /usr/bin/env php -r "copy('https://getcomposer.org/installer', 'composer-
setup.php');"  
RUN /usr/bin/env php composer-setup.php \--install-dir=/usr/bin
\--filename=composer  
RUN /usr/bin/env chmod +x /usr/bin/composer  
RUN /usr/bin/env php -r "unlink('composer-setup.php');"  

