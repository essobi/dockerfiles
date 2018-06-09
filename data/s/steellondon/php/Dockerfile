FROM php:7.1-apache  
MAINTAINER Giovanni Derks <giovanni.derks@steellondon.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY config/php.ini /usr/local/etc/php/  
  
RUN apt-get update && apt-get install -y \  
git \  
libmcrypt-dev \  
libtidy-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libxml2-dev \  
locales  
  
# Ensure that we have the UTF-8 British and American English locale  
RUN sed -ri 's/#(.*en_GB\\.UTF.*)$/\1/' /etc/locale.gen && \  
sed -ri 's/#(.*en_US\\.UTF.*)$/\1/' /etc/locale.gen  
RUN locale-gen  
  
# Install PHP Extensions  
RUN docker-php-ext-install pdo_mysql mcrypt tidy mbstring soap zip  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd  
  
RUN a2enmod rewrite  
  
RUN php -r "readfile('https://getcomposer.org/installer');" > composer-
setup.php && \  
php -r "if (hash('SHA384', file_get_contents('composer-setup.php')) ===
'55d6ead61b29c7bdee5cccfb50076874187bd9f21f65d8991d46ec5cc90518f447387fb9f76ebae1fbbacf329e583e30')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/local/bin --filename=composer && \  
php -r "unlink('composer-setup.php');" && \  
chmod +x /usr/local/bin/composer

