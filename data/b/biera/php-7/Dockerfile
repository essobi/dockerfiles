FROM php:7  
MAINTAINER Jakub Biernacki <kubiernacki@gmail.com>  
  
# ESSENTIAL TOOLS  
RUN apt-get update && apt-get install -y git htop nano  
  
# INSTALL ESSENTIALS LIBS TO COMPILE PHP EXTENSTIONS  
RUN apt-get update && apt-get install -y \  
# for zip ext  
zlib1g-dev \  
  
# for pg_pgsql ext  
libpq-dev \  
  
# for soap and xml related ext  
libxml2-dev \  
  
# for xslt ext  
libxslt-dev \  
  
# for gd ext  
libjpeg-dev libpng-dev \  
  
# for intl ext  
libicu-dev  
  
# INSTALL PHP EXTENSIONS VIA docker-php-ext-install script  
# installed by default: curl, json  
RUN docker-php-ext-install bcmath  
RUN docker-php-ext-install calendar  
RUN docker-php-ext-install ctype  
RUN docker-php-ext-install dba  
RUN docker-php-ext-install dom  
RUN docker-php-ext-install exif  
RUN docker-php-ext-install fileinfo  
RUN docker-php-ext-install ftp  
RUN docker-php-ext-install gettext  
RUN docker-php-ext-install gd  
RUN docker-php-ext-install hash  
RUN docker-php-ext-install iconv  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install opcache  
RUN docker-php-ext-install pcntl  
RUN docker-php-ext-install pdo  
RUN docker-php-ext-install pdo_pgsql  
RUN docker-php-ext-install posix  
RUN docker-php-ext-install session  
RUN docker-php-ext-install shmop  
RUN docker-php-ext-install simplexml  
RUN docker-php-ext-install soap  
RUN docker-php-ext-install sockets  
RUN docker-php-ext-install xsl  
RUN docker-php-ext-install zip  
  
# RUN docker-php-ext-install snmp  
# RUN docker-php-ext-install recode  
# RUN docker-php-ext-install ldap  
# RUN docker-php-ext-install mcrypt  
# RUN docker-php-ext-install mssql  
# RUN docker-php-ext-install mysql  
# RUN docker-php-ext-install mysqli  
# RUN docker-php-ext-install oci8  
# RUN docker-php-ext-install odbc  
# RUN docker-php-ext-install imap  
# RUN docker-php-ext-install interbase  
# RUN docker-php-ext-install enchant  
# RUN docker-php-ext-install filter  
# RUN docker-php-ext-install bz2  
# RUN docker-php-ext-install gmp  
# RUN docker-php-ext-install pdo_dblib  
# RUN docker-php-ext-install pdo_firebird  
# RUN docker-php-ext-install pdo_mysql  
# RUN docker-php-ext-install pdo_oci  
# RUN docker-php-ext-install pdo_odbc  
# RUN docker-php-ext-install pdo_sqlite  
# RUN docker-php-ext-install pgsql  
# RUN docker-php-ext-install phar  
# RUN docker-php-ext-install pspell  
# RUN docker-php-ext-install standard  
# RUN docker-php-ext-install sybase_ct  
# RUN docker-php-ext-install sysvmsg  
# RUN docker-php-ext-install sysvsem  
# RUN docker-php-ext-install sysvshm  
# RUN docker-php-ext-install tidy  
# RUN docker-php-ext-install wddx  
# RUN docker-php-ext-install xml  
# RUN docker-php-ext-install xmlreader  
# RUN docker-php-ext-install xmlrpc  
# RUN docker-php-ext-install xmlwriter  
# ADD PHP.INI (SUITABLE FOR DEVELOPMENT)  
ADD php.ini /usr/local/etc/php  
  
# INSTALL XDEBUG  
RUN pecl install xdebug  
RUN cp /usr/local/etc/php/php.ini /usr/local/etc/php/php-with-xdebug.ini \  
&& echo -e "\n[xdebug]\nzend_extension=/usr/local/lib/php/extensions/no-debug-
non-
zts-20151012/xdebug.so\nxdebug.remote_enable=1\nxdebug.remote_connect_back=1"
>> /usr/local/etc/php/php-with-xdebug.ini \  
&& echo "alias xdebug='php -c /usr/local/etc/php/php-with-xdebug.ini'" >>
/etc/bash.bashrc  
  
# COMPOSER  
ENV COMPOSER_HOME /usr/local/composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php --install-dir=/usr/bin --filename=composer  
RUN rm composer-setup.php  
ADD composer.json /usr/local/composer  
RUN echo "export COMPOSER_HOME=/usr/local/composer" >> /etc/bash.bashrc  
  
# INSTALL ROBO TASK RUNNER  
RUN composer global require codegyre/robo  
  
# DOWNLOAD SYMFONY INSTALLER  
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony && chmod
a+x /usr/local/bin/symfony  
  
# CLEAN APT AND TMP  
RUN apt-get clean && apt-get autoremove && rm -rf /var/lib/apt/lists/* /tmp/*
/var/tmp/*  

