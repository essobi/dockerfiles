# See https://github.com/docker-
library/php/blob/4677ca134fe48d20c820a19becb99198824d78e3/7.0/fpm/Dockerfile  
FROM php:7.2-fpm  
  
RUN apt-get update && apt-get install -y \  
autoconf \  
coreutils \  
git \  
libcurl4-gnutls-dev \  
libicu-dev \  
libmcrypt-dev \  
libpng-dev \  
libvpx-dev \  
libxpm-dev \  
libxml2-dev \  
openntpd \  
tzdata \  
unzip  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
# Set timezone  
RUN rm /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime  
RUN "date"  
  
# Install mCrypt  
RUN pecl install mcrypt-1.0.1  
RUN docker-php-ext-enable mcrypt  
  
# Type docker-php-ext-install to see available extensions  
RUN docker-php-ext-install -j$(nproc) gd iconv pdo pdo_mysql curl bcmath \  
mbstring json xml xmlrpc zip intl opcache  
  
# Add php.ini and opcache configuration  
ADD php.ini /usr/local/etc/php/  
ADD opcache.ini /usr/local/etc/php/conf.d/  

