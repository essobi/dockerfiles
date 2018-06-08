FROM php:5-apache  
MAINTAINER porchn <pichai.chin@gmail.com>  
  
ENV TZ=Asia/Bangkok  
  
# Set the timezone.  
RUN echo $TZ > /etc/timezone  
RUN dpkg-reconfigure -f noninteractive tzdata  
RUN mkdir -p /etc/apache2/ssl  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmemcached-dev \  
libicu-dev \  
openssl \  
&& pecl install memcached \  
&& docker-php-ext-enable memcached \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd iconv mcrypt intl mysql mysqli
pdo_mysql zip mbstring  
  
#bcmath bz2 calendar ctype curl dba dom enchant exif fileinfo filter ftp gd
gettext gmp hash iconv imap interbase intl json ldap mbstring mcrypt mssql
mysql mysqli oci8 odbc opcache pcntl pdo pdo_dblib pdo_firebird pdo_mysql
pdo_oci pdo_odbc pdo_pgsql pdo_sqlite pgsql phar posix pspell readline recode
reflection session shmop simplexml snmp soap sockets spl standard sybase_ct
sysvmsg sysvsem sysvshm tidy tokenizer wddx xml xmlreader xmlrpc xmlwriter xsl
zip  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Enable Apache mod_rewrite  
RUN a2enmod rewrite  
  
# Enable ssl  
RUN a2enmod ssl  
RUN a2enmod headers  
  
VOLUME ['/etc/apache2/sites-available','/var/www','/var/log/apache2']  
  
EXPOSE 80  
EXPOSE 443

