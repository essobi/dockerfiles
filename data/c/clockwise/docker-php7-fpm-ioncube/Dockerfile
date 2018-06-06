FROM php:7.0-fpm  
  
MAINTAINER Ihor Omelchenko <megapixel23@gmail.com>  
  
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');"  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer && \  
rm -rf /tmp/composer-setup.php  
  
RUN apt-get update && \  
apt-get install -y git unzip  
  
RUN apt-get update && \  
apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libsqlite3-dev \  
libcurl4-gnutls-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt gd pdo_mysql pcntl
pdo_sqlite zip curl bcmath opcache mbstring \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-enable iconv mcrypt gd pdo_mysql pcntl pdo_sqlite zip curl
bcmath opcache mbstring \  
&& apt-get autoremove -y  
  
RUN cd /tmp \  
&& curl -o ioncube.tar.gz
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& tar -xvvzf ioncube.tar.gz \  
&& mv ioncube/ioncube_loader_lin_7.0.so /usr/local/lib/php/extensions/* \  
&& rm -Rf ioncube.tar.gz ioncube \  
&& echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20151012/ioncube_loader_lin_7.0.so" > /usr/local/etc/php/conf.d/00_docker-
php-ext-ioncube_loader_lin_7.0.ini  
  
WORKDIR /var/www  
  
EXPOSE 9000  
CMD ["php-fpm"]

