# See https://github.com/docker-
library/php/blob/4677ca134fe48d20c820a19becb99198824d78e3/7.0/fpm/Dockerfile  
FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y \  
git \  
unzip  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
# Set timezone  
RUN rm /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Minsk /etc/localtime  
RUN "date"  
  
# Type docker-php-ext-install to see available extensions  
RUN docker-php-ext-install pdo pdo_mysql  
  
# Install GD  
RUN apt-get install -y libfreetype6-dev libjpeg62-turbo-dev libpng12-dev  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd  
  
# Install mbstring  
RUN docker-php-ext-install mbstring  
  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_connect_back=1" >> /usr/local/etc/php/conf.d/xdebug.ini
\  
&& echo "xdebug.idekey = PHPSTORM" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_port = 9000" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_host = 172.30.33.56" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_log=/var/www/xdebug.log" >>
/usr/local/etc/php/conf.d/xdebug.ini  
  
RUN echo 'alias sf="php app/console"' >> ~/.bashrc  
RUN echo 'alias sf3="php bin/console"' >> ~/.bashrc  
  
WORKDIR /var/www/html/docroot  
  
RUN apt-get update && apt-get -y install nano

