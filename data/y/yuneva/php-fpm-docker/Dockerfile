FROM ubuntu:17.10  
RUN apt-get update && apt-get install -my \  
curl \  
wget \  
php-curl \  
php-fpm \  
php-gd \  
php-xsl \  
php-mysqlnd \  
php-mcrypt \  
php-cli \  
php-intl \  
php-bz2 \  
php-zip \  
php-mbstring \  
php-bcmath \  
git \  
zip \  
php-apcu \  
php-redis \  
php-opcache  
  
RUN mkdir /run/php  
  
ADD conf/www.conf /etc/php/7.1/fpm/pool.d/www.conf  
ADD conf/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf  
ADD conf/memory.ini /etc/php/7.1/fpm/conf.d/memory.ini  
ADD conf/apcu.ini /etc/php/7.1/fpm/conf.d/apcu.ini  
ADD conf/opcache.ini /etc/php/7.1/fpm/conf.d/opcache.ini  
ADD conf/upload_max_filesize.ini
/etc/php/7.1/fpm/conf.d/upload_max_filesize.ini  
ADD conf/datetimezone.ini /etc/php/7.1/fpm/conf.d/datetimezone.ini  
ADD conf/datetimezone.ini /etc/php/7.1/cli/conf.d/datetimezone.ini  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/local/bin/composer  
RUN chmod +x /usr/local/bin/composer  
RUN ln -snf /usr/share/zoneinfo/Europe/Lisbon /etc/localtime  
  
WORKDIR /var/www/html/countit-web-symfony  
  
EXPOSE 9000  
CMD ["php-fpm7.1"]  

