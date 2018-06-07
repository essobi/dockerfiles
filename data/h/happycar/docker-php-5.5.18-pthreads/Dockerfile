FROM ubuntu:12.04  
  
MAINTAINER Kevin Luecke <kevin.luecke@happycar.de>  
  
# update and install packages  
RUN apt-get -qq update && apt-get -qq upgrade -y  
RUN apt-get -qq install -y libxml2 libxml2-dev libssl-dev pkg-config curl
libcurl4-nss-dev enchant libenchant-dev libjpeg8 libjpeg8-dev libpng12-0
libpng12-dev libvpx1 libvpx-dev libfreetype6 libfreetype6-dev libt1-5
libt1-dev libgmp10 libgmp-dev libicu48 libicu-dev mcrypt libmcrypt4 libmcrypt-
dev libpspell-dev libedit2 libedit-dev libsnmp15 libsnmp-dev libxslt1.1
libxslt1-dev checkinstall autoconf wget mysql-server php5-mysql  
  
# recompile php 5.5.18  
RUN wget http://de1.php.net/get/php-5.5.18.tar.gz/from/this/mirror -O
php-5.5.18.tar.gz && tar -xzvf php-5.5.18.tar.gz  
WORKDIR /php-5.5.18  
RUN ./configure --enable-debug --enable-maintainer-zts --enable-pthreads
--with-mysqli=mysqlnd && make && checkinstall && cp php.ini-production
/usr/local/lib/php.ini  
  
RUN pear config-set php_ini /usr/local/lib/php.ini  
RUN pecl config-set php_ini /usr/local/lib/php.ini  
RUN pecl install pthreads  

