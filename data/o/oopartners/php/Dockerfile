FROM php:7-apache  
  
ENV APPLICATION_ENV production  
  
RUN apt-get update  
RUN apt-get install -y g++  
  
# pour ext intl  
RUN apt-get install -y libicu-dev  
RUN docker-php-ext-install intl  
  
# pour ext imap  
RUN apt-get install -y openssl  
RUN apt-get install -y libc-client-dev  
RUN apt-get install -y libkrb5-dev  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl  
RUN docker-php-ext-install imap  
  
RUN apt-get install -y libxml2-dev  
RUN docker-php-ext-install dom  
  
RUN apt-get install -y libfreetype6-dev  
RUN apt-get install -y libgd-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr  
# exif pour gregwar/image ?  
RUN docker-php-ext-install gd exif  
  
RUN docker-php-ext-install mysqli pdo pdo_mysql  
  
RUN apt-get install -y libmcrypt-dev  
RUN docker-php-ext-install mcrypt  
  
RUN docker-php-ext-install gettext mbstring soap  
  
# Pour C&P et composer  
RUN docker-php-ext-install zip  
  
RUN docker-php-ext-install ftp  
  
# pour ext ldap  
# RUN apt-get install -y libldap2-dev  
# RUN docker-php-ext-configure ldap --prefix=/usr/local/php --with-
ldap=/usr/lib/i386-linux-gnu  
# RUN docker-php-ext-install ldap  
# ext bcmath pour client RabbitMQ  
RUN docker-php-ext-configure bcmath  
RUN docker-php-ext-install bcmath  
  
# ext curl pour elasticsearch  
RUN apt-get install -y libcurl4-openssl-dev  
RUN docker-php-ext-install curl  
  
COPY ./php.ini /usr/local/etc/php/php.ini  
  
# Opcache  
# RUN pecl install -o -f zendopcache \  
# && echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20100525/opcache.so" > /usr/local/etc/php/conf.d/opcache.ini  
# xdebug  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
  
# APC  
RUN pear config-set php_ini /usr/local/etc/php/php.ini  
RUN pecl config-set php_ini /usr/local/etc/php/php.ini  
RUN pecl install apcu  
  
RUN a2enmod rewrite  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs build-essential  
RUN npm install -g phantomjs casperjs  
  
RUN apt-get autoremove -y && apt-get clean all  
  
VOLUME ["/u"]  
  
COPY apache2.development.conf /etc/apache2/apache2.development.conf  
COPY apache2.production.conf /etc/apache2/apache2.production.conf  
  
CMD apache2 -DFOREGROUND -f /etc/apache2/apache2.$APPLICATION_ENV.conf  

