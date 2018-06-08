FROM ubuntu:17.10  
RUN apt-get update && apt-get install -my \  
acl \  
curl \  
wget \  
git \  
zip \  
php-curl \  
php-fpm \  
php-gd \  
php-xsl \  
php-mysqlnd \  
php-mcrypt \  
php-xdebug \  
php-cli \  
php-intl \  
php-bz2 \  
php-zip \  
php-mbstring \  
php-apcu \  
php-opcache  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get remove cmdtest  
RUN apt-get update  
RUN apt-get install -y nodejs yarn  
  
RUN mkdir /run/php  
  
ADD conf/www.conf /etc/php/7.1/fpm/pool.d/www.conf  
ADD conf/memory.ini /etc/php/7.1/fpm/conf.d/memory.ini  
ADD conf/upload_max_filesize.ini
/etc/php/7.1/fpm/conf.d/upload_max_filesize.ini  
ADD conf/opcache.ini /etc/php/7.1/mods-available/10-opcache.ini  
ADD conf/apcu.ini /etc/php/7.1/mods-available/20-apcu.ini  
ADD conf/apcu.ini /etc/php/7.1/mods-available/20-apcu_bc.ini  
ADD conf/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer  
RUN php -r "unlink('composer-setup.php');"  
  
WORKDIR /var/www/html/naturmedicus  
  
EXPOSE 9000  
CMD ["php-fpm7.1"]  

