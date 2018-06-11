FROM php:7.1-apache  
  
RUN a2enmod vhost_alias  
RUN a2enmod rewrite  
RUN a2enmod ssl  
  
# APC  
RUN pear config-set php_ini /usr/local/etc/php/php.ini  
RUN pecl config-set php_ini /usr/local/etc/php/php.ini  
RUN pecl install apc redis memcached xdebug  
  
RUN apt-get update && apt-get install -y \  
openssl \  
mysql-client \  
libapache2-mod-fcgid \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
sendmail \  
git \  
libmemcached-dev \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install opcache \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-enable xdebug  
  
#MEMCACHED  
RUN git clone \--branch php7 https://github.com/php-memcached-dev/php-
memcached /usr/src/php/ext/memcached \  
&& cd /usr/src/php/ext/memcached \  
&& docker-php-ext-configure memcached \  
&& docker-php-ext-install memcached \  
&& docker-php-ext-install pcntl \  
&& docker-php-ext-install bcmath  
  
RUN ( \  
echo "opcache.memory_consumption=128"; \  
echo "opcache.interned_strings_buffer=8"; \  
echo "opcache.max_accelerated_files=4000"; \  
echo "opcache.revalidate_freq=60"; \  
echo "opcache.fast_shutdown=1"; \  
echo "opcache.enable_cli=1"; \  
) > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
#SSL CONFIG  
RUN mkdir -p /usr/local/apache/conf  
ADD ssl/server.crt /usr/local/apache/conf/ssl.crt  
ADD ssl/server.key /usr/local/apache/conf/ssl.key  
  
RUN service apache2 restart  
  
RUN apt-get update && apt-get install -y \  
zip \  
unzip  
  
#Composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php --install-dir=/usr/local/bin  
RUN php -r "unlink('composer-setup.php');"  
  
RUN mv /usr/local/bin/composer.phar /usr/local/bin/composer && chmod +x
/usr/local/bin/composer  
  
RUN composer global require phpunit/phpunit \  
&& ln -s /root/.composer/vendor/bin/phpunit /usr/local/bin/phpunit  
  
RUN composer global require phpmetrics/phpmetrics \  
&& ln -s /root/.composer/vendor/bin/phpmetrics /usr/local/bin/phpmetrics  
  
RUN composer global require squizlabs/php_codesniffer \  
&& ln -s /root/.composer/vendor/bin/phpcs /usr/local/bin/phpcs  
#RUN phpunit -v  
EXPOSE 80  
EXPOSE 443  

