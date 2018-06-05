FROM php:7.2-apache  
  
COPY dk-vhosts.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Install required extensions  
RUN apt-get update && apt-get install -y \  
locales \  
git wget unzip \  
libmcrypt-dev \  
zlib1g-dev \  
gettext \  
libfreetype6 libfreetype6-dev \  
libjpeg62 libjpeg62-turbo-dev \  
libpng-dev \  
\--no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
  
RUN docker-php-ext-install -j$(nproc) zip mysqli pdo_mysql  
  
RUN ["/bin/bash", "-c", "docker-php-ext-configure gd --with-freetype-
dir=/usr/include/ --with-jpeg-dir=/usr/include/"]  
RUN docker-php-ext-install -j$(nproc) gd  
  
# Install PHP extensions  
RUN a2enmod rewrite && a2enmod headers  
  
# Install Composer  
RUN wget
https://raw.githubusercontent.com/composer/getcomposer.org/master/web/installer
-O - -q | php -- --quiet  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install PHPUnit  
RUN wget https://phar.phpunit.de/phpunit.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
  
# Set default volume for image  
# This would be overrided by docker-compose for updatable source code between
development  
COPY . /data  
WORKDIR /data  
  
# Fixes user permissions for Mac OS
[https://github.com/boot2docker/boot2docker/issues/581]  
RUN usermod -u 1000 www-data  
  
# Inherit from based image  
CMD ["apache2-foreground"]

