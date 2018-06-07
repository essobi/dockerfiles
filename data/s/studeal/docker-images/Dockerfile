FROM php:5.6  
RUN apt-get update && apt-get install -y \  
unzip \  
zip \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
wkhtmltopdf \  
libpcre3-dev \  
libmcrypt-dev  
  
RUN docker-php-ext-install -j$(nproc) mcrypt  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
  
RUN docker-php-ext-install -j$(nproc) gd mcrypt  
  
RUN echo "date.timezone=\"Europe/Paris\"" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
RUN docker-php-ext-install zip  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN composer global require hirak/prestissimo  

