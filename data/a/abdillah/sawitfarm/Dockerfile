FROM milk/php-xdebug:7.1  
  
RUN apt-get update -yqq && apt-get install -yqq libcurl4-gnutls-dev libicu-dev
libvpx-dev libjpeg-dev libpng-dev libxpm-dev libfreetype6-dev libxml2-dev
libexpat1-dev libbz2-dev libgmp3-dev libldap2-dev unixodbc-dev libsqlite3-dev
libaspell-dev libsnmp-dev libpcre3-dev libtidy-dev  
  
RUN docker-php-ext-install pdo_mysql sockets intl  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  

