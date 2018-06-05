FROM php:7.2-fpm  
  
RUN export buildDeps='gcc libc6-dev make libfreetype6-dev libjpeg62-turbo-dev
libmcrypt-dev libpng-dev libjpeg62-turbo-dev libjpeg-dev libmcrypt-dev libpng-
dev icu-devtools libicu-dev libbz2-dev' && \  
apt-get update && \  
apt-get install -y $buildDeps \  
icu-doc libicu57 libmcrypt-dev \  
bzip2 \  
git \  
unzip \  
wget \  
netcat && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd && \  
docker-php-ext-configure bz2 --with-bz2 && \  
docker-php-ext-install -j$(nproc) bz2 && \  
docker-php-ext-configure mysqli --with-mysqli=mysqlnd && \  
docker-php-ext-install -j$(nproc) mysqli && \  
docker-php-ext-install -j$(nproc) iconv intl zip exif pdo_mysql && \  
pecl install mcrypt-1.0.1 && \  
docker-php-ext-enable mcrypt && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# not yet working:  
# apt-get purge -y --auto-remove $buildDeps && \  
  
COPY www.conf /usr/local/etc/php-fpm.d/www.conf  
COPY docker-php-settings.ini /usr/local/etc/php/conf.d/docker-php-settings.ini  
COPY startup.sh /startup.sh  
  
CMD ["/bin/bash","/startup.sh"]  
  

