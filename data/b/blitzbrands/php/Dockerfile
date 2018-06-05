FROM php:5.6-fpm  
  
ENV WORKDIR /var/www/html  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
php-pear \  
git \  
zlib1g-dev \  
mysql-client \  
libicu-dev \  
cron \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd zip bz2 mbstring pdo_mysql intl \  
&& pecl install apcu-4.0.10 && echo "extension=apcu.so" >
/usr/local/etc/php/conf.d/acpu.ini  
  
COPY php-fpm.conf /usr/local/etc/  
  
# Set environmental variables  
ENV COMPOSER_HOME /root/composer  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN export PATH=/root/composer/.composer/vendor/bin:$PATH  
RUN mkdir -p /usr/local/etc/php-fpm.d  

