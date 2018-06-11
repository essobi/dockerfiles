FROM php:7.0-apache  
  
RUN apt-get update && apt-get install -y \  
unzip \  
wget \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install -j5 bcmath gd mysqli pdo_mysql mcrypt  
  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "[xdebug]" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.idekey = "PHPSTORM"" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable = 1" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_host = 172.17.0.1" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_connect_back = 1" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.connect_back = 1" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.profiler_enable=1" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.profiler_output_dir=/var/www/profile" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.profiler_enable_trigger=1" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
RUN echo "expose_php = Off" >> /usr/local/etc/php/php.ini  
  
ADD ["etc/apache2/sites-enabled", "/etc/apache2/sites-enabled"]  
ADD ["etc/apache2/conf-enabled/security.conf", "/etc/apache2/conf-
enabled/security.conf"]  
  
#RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout
/etc/ssl/private/ssl-cert.key -out /etc/ssl/certs/ssl-cert.pem -subj
"/C=CN/ST=Shanghai/L=Shanghai/O=Security/OU=Development/CN=hawk.com"  
RUN a2enmod rewrite  
#RUN a2ensite default-ssl  
RUN a2enmod ssl  
RUN a2enmod headers  
  
EXPOSE 80  
EXPOSE 443  

