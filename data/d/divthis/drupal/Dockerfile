FROM php:5.6-fpm  
  
# Update APT and PECL cache  
RUN apt-get update  
  
# Install GD Extension  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/us \  
&& docker-php-ext-install gd \  
&& apt-get purge -y libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev  
  
# Install graphicsmagick  
RUN apt-get install -y graphicsmagick  
  
# Install pspell Extension  
RUN apt-get install -y libpspell-dev \  
&& docker-php-ext-install pspell \  
&& apt-get purge -y libpspell-dev  
  
# Install snmp Extension  
RUN apt-get install -y libsnmp-dev \  
&& docker-php-ext-install snmp \  
&& apt-get purge -y libsnmp-dev  
  
# Install xsl Extension  
RUN apt-get install -y libxslt1-dev \  
&& docker-php-ext-install xsl \  
&& apt-get purge -y libxslt1-dev  
  
# Install apcu Extension  
RUN yes "" | pecl install channel://pecl.php.net/APCu-4.0.7 \  
&& echo "extension=apcu.so" > /usr/local/etc/php/conf.d/ext-apcu.ini  
  
# Install memcache Extension  
RUN yes "" | pecl install memcache \  
&& echo "extension=memcache.so" > /usr/local/etc/php/conf.d/ext-memcache.ini  
  
# Install additional Extensions  
RUN docker-php-ext-install \  
opcache \  
sockets \  
mysql \  
mysqli \  
pdo_mysql \  
xmlrpc \  
mbstring \  
zip  
  
# Install git for use with composer  
RUN apt-get -y install git  
  
# Install Composer  
RUN apt-get install snmp \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& echo 'export PATH="$HOME/.composer/vendor/bin:$PATH"' >> ~/.bashrc  
  
# Install MariaDB client for use with Drush  
RUN apt-get install mariadb-client-core-10.0 -y  
  
# Install Drush  
RUN composer global require drush/drush:7.* --prefer-source  
  
# Set Drupal tar.gz file to download  
ENV DRUPAL_TARGZ http://ftp.drupal.org/files/projects/drupal-7.59.tar.gz  
  
# Install Drupal  
RUN curl -SL ${DRUPAL_TARGZ} -o drupal.tar.gz \  
&& tar -xof drupal.tar.gz -C /var/www/html --strip-components=1 \  
&& rm drupal.tar.gz  
  
# Copy php.ini  
COPY php.ini /usr/local/etc/php/

