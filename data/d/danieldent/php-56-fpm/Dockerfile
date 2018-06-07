FROM php:5.6-fpm  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libcurl4-nss-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install curl \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install pdo \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install json \  
&& cd /tmp \  
&& curl -o ioncube.tar.gz
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
\  
&& echo "dacf7351cb750e999a59c8167d8057a8d2ca72d2391b74444db1b251a76c2fba
ioncube.tar.gz"|shasum -c \  
&& tar -xvvzf ioncube.tar.gz \  
&& mv ioncube/ioncube_loader_lin_5.6.so /usr/local/lib/php/extensions/* \  
&& rm -Rf ioncube.tar.gz ioncube \  
&& echo "zend_extension=ioncube_loader_lin_5.6.so" >
/usr/local/etc/php/conf.d/00_docker-php-ext-ioncube_loader_lin_5.6.ini  
CMD ["/usr/local/sbin/php-fpm", "--nodaemonize"]  

