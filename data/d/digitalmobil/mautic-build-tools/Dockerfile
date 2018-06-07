FROM php:5.6-cli  
MAINTAINER tuschl@digitalmobil.com  
  
RUN adduser --gecos "" \--disabled-password --home /home/mautic-build mautic-
build  
  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \  
ssh sudo subversion git bzip2 zip unzip \  
libfreetype6-dev \  
libjpeg-dev \  
libkrb5-dev \  
libmcrypt-dev \  
libpng-dev \  
libssl-dev \  
libwebp-dev \  
libxpm-dev \  
libc-client-dev \  
libicu-dev \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN docker-php-ext-configure imap --with-imap --with-imap-ssl --with-kerberos  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
  
RUN docker-php-ext-install gd imap intl mbstring mcrypt mysqli pdo pdo_mysql
zip  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php -r "copy('https://composer.github.io/installer.sig', 'composer-
setup.sig');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
trim(file_get_contents('composer-setup.sig'))) { echo 'Installer verified'; }
else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo
PHP_EOL;" && \  
php composer-setup.php --filename=composer --install-dir=/bin && \  
php -r "unlink('composer-setup.sig');" && \  
php -r "unlink('composer-setup.php');"  
  
RUN php -r "copy('https://github.com/interconnectit/Search-Replace-
DB/archive/master.zip', '/Search-Replace-DB-master.zip');" && \  
unzip /Search-Replace-DB-master.zip && \  
php -r "unlink('/Search-Replace-DB-master.zip');" && \  
chmod +x /Search-Replace-DB-master/srdb.cli.php && \  
sed -i -E 's:/usr/bin/php:/usr/local/bin/php:g' /Search-Replace-DB-
master/srdb.cli.php && \  
ln -s /Search-Replace-DB-master/srdb.cli.php /usr/bin/srdb  
  
# Define working directory.  
WORKDIR /data  
  
COPY entrypoint.sh /entrypoint.sh  
# Define default command.  
CMD ["bash"]  
ENTRYPOINT ["/entrypoint.sh"]  

