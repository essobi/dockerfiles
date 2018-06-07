FROM php:7.1.17  
LABEL maintainer "Víctor Falcón <victoor89@gmail.com>" \  
php="7.1.17"  
  
RUN apt-get update && apt-get install -y zip unzip libfreetype6-dev
libjpeg62-turbo-dev libmcrypt-dev \  
libpng-dev mysql-client zlib1g-dev libxpm4 libxrender1 libgtk2.0-0 libnss3
libgconf-2-4 chromium xvfb \  
gtk2-engines-pixbuf xfonts-cyrillic xfonts-100dpi xfonts-75dpi xfonts-base
xfonts-scalable imagemagick \  
x11-apps  
RUN docker-php-ext-install -j$(nproc) iconv mcrypt  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install -j$(nproc) gd  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install zip  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer

