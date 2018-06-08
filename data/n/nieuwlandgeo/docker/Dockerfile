FROM circleci/php:7.1-cli-node-browsers  
  
USER root  
  
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=866729  
RUN mkdir -p /usr/share/man/man7  
  
RUN apt-get update  
RUN apt-get install -y apt-utils  
  
RUN apt-get install -y libpq-dev libpng-dev unzip postgresql-client libbz2-dev
libicu-dev gdal-bin  
  
RUN docker-php-ext-install -j$(nproc) gd pdo_pgsql zip bcmath bz2 gettext intl
sockets  
  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php -r "copy('https://composer.github.io/installer.sig', 'composer-
setup.sig');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
trim(file_get_contents('composer-setup.sig'))) { echo 'Installer verified'; }
else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo
PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& mv composer.phar /usr/local/bin/composer  
  
ADD php.ini /usr/local/etc/php/  
  
USER circleci  

