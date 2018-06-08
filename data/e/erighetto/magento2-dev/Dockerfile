FROM php:7.1-apache  
  
MAINTAINER Emanuel Righetto <posta@emanuelrighetto.it>  
  
RUN apt-get update \  
&& apt-get install -y \  
libfreetype6-dev \  
libicu-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
git \  
nano \  
wget \  
lynx \  
psmisc \  
mysql-client \  
&& apt-get clean  
  
RUN docker-php-ext-configure \  
gd --with-freetype-dir=/usr/include/ \--with-jpeg-dir=/usr/include/; \  
docker-php-ext-install \  
gd \  
intl \  
mbstring \  
mcrypt \  
pdo_mysql \  
xsl \  
zip \  
opcache \  
soap  
  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& docker-php-source delete  
  
RUN { \  
echo ';;;;;;;;;; Recommended PHP.ini settings ;;;;;;;;;;'; \  
echo 'memory_limit = 768M'; \  
echo 'upload_max_filesize = 64M'; \  
echo 'post_max_size = 64M'; \  
echo 'max_execution_time = 18000'; \  
echo 'date.timezone = Europe/Rome'; \  
echo 'error_reporting = E_ALL & ~E_NOTICE & ~E_WARNING'; \  
echo ';;;;;;;;;; xDebug ;;;;;;;;;;'; \  
echo 'xdebug.remote_enable = 1'; \  
echo 'xdebug.idekey = "phpstorm"'; \  
echo 'xdebug.remote_port = 9000'; \  
echo 'xdebug.remote_autostart = 0'; \  
echo 'xdebug.profiler_enable = 0'; \  
echo 'xdebug.remote_connect_back = 1'; \  
echo 'xdebug.remote_handler=dbgp'; \  
echo 'xdebug.max_nesting_level = 256'; \  
echo ';xdebug.remote_cookie_expire_time = -9999'; \  
} >> /usr/local/etc/php/conf.d/custom-php-settings.ini  
  
RUN usermod -u 1000 www-data; \  
a2enmod rewrite; \  
curl -o /tmp/composer-setup.php https://getcomposer.org/installer; \  
curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig; \  
php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php')) !==
trim(file_get_contents('/tmp/composer-setup.sig'))) { unlink('/tmp/composer-
setup.php'); echo 'Invalid installer' . PHP_EOL; exit(1); }"; \  
php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer; \  
rm /tmp/composer-setup.php; \  
chmod +x /usr/local/bin/composer;  
  
RUN mkdir -p /root/.composer  
  
EXPOSE 80 443 9000  
  
WORKDIR /var/www/html  

