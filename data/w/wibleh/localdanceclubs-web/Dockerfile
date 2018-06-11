FROM php:7.1-apache  
  
RUN apt-get update && apt-get install -y \  
curl \  
git \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmagickwand-dev \  
mariadb-client \  
supervisor \  
vim \  
wget  
  
RUN docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
  
RUN docker-php-ext-install \  
gd \  
mbstring \  
mcrypt \  
opcache \  
pdo_mysql \  
zip  
  
RUN pecl install imagick  
RUN docker-php-ext-enable imagick  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN rm -rf /var/www/html  
WORKDIR /var/www/  
  
RUN a2enmod rewrite  
  
EXPOSE 80  

