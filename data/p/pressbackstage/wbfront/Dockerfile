FROM php:5-apache  
  
RUN apt-get update && apt-get -y install libfreetype6-dev libjpeg62-turbo-dev
libmcrypt-dev libpng12-dev libcurl4-openssl-dev && docker-php-ext-install
-j$(nproc) pdo_mysql mbstring mcrypt curl mysqli && docker-php-ext-configure
gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ && docker-
php-ext-install -j$(nproc) gd && apt-get clean all  
  
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/
&& ln -s /etc/apache2/mods-available/socache_shmcb.load /etc/apache2/mods-
enabled/ && ln -s /etc/apache2/mods-available/ssl.load /etc/apache2/mods-
enabled/ && ln -s /etc/apache2/mods-available/ssl.conf /etc/apache2/mods-
enabled/  
  
RUN mkdir /etc/apache2/conf && touch /etc/apache2/conf/php.ini && ln -s
/etc/apache2/conf/php.ini /usr/local/etc/php/ && touch
/etc/apache2/conf/wb.conf && ln -s /etc/apache2/conf/wb.conf
/etc/apache2/conf-enabled/ && touch /etc/apache2/conf/default-ssl.conf && ln
-s /etc/apache2/conf/default-ssl.conf /etc/apache2/sites-enabled/  

