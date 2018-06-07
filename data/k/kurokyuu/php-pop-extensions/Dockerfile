FROM php:7.1.1  
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*  
  
RUN \  
apt-get update && apt-get install -y libpq5 mariadb-client libpq-dev libpng-
dev libjpeg62-turbo libjpeg-dev libfreetype6 libfreetype6-dev libmcrypt4
libmcrypt-dev && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include \--with-jpeg-
dir=/usr/include && \  
docker-php-ext-install -j$(nproc) iconv mbstring gettext zip mcrypt gd
pdo_mysql pdo_pgsql bcmath && \  
apt-get remove -y libpq-dev libpng-dev libjpeg-dev libfreetype6-dev libmcrypt-
dev && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*  
# PECL extensions  
RUN \  
apt-get update && apt-get install -y libssl-dev && \  
pecl install --onlyreqdeps --force mongodb xdebug && rm -rf /tmp/pear &&
docker-php-ext-enable mongodb xdebug && \  
apt-get remove -y libssl-dev && rm -rf /var/lib/apt/lists/*  
# composer  
RUN \  
php -r "copy('https://getcomposer.org/installer', '/tmp/composer-setup.php');"
&& \  
php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
&& \  
rm /tmp/composer-setup.php  
  

