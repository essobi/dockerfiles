FROM php:7.2-fpm  
  
RUN apt-get update  
  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
libxml2-dev \  
libicu-dev \  
libz-dev \  
libmemcached-dev \  
unzip \  
less \  
git  
  
RUN apt-get clean  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) opcache pdo pdo_mysql iconv soap zip intl
gd  
  
RUN pecl install memcached \  
&& echo "extension=memcached.so" >> /usr/local/etc/php/conf.d/memcached.ini  
  
RUN yes | pecl install xdebug  
  
# Install Composer  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/installer.php');"
\  
&& php /tmp/installer.php --no-ansi --install-dir=/usr/bin --filename=composer
\  
&& composer --ansi --version --no-interaction  
  
# Install PHP CS Fixer  
RUN curl -L https://github.com/FriendsOfPHP/PHP-CS-
Fixer/releases/download/v1.13.1/php-cs-fixer.phar -o php-cs-fixer \  
&& chmod a+x php-cs-fixer \  
&& mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
# Install CodeCeption  
RUN curl -L http://codeception.com/codecept.phar -o codecept \  
&& chmod a+x codecept \  
&& mv codecept /usr/local/bin/codecept  
  
# Install PHP Stan  
RUN curl -L
https://github.com/phpstan/phpstan/releases/download/0.8/phpstan.phar -o
phpstan \  
&& chmod a+x phpstan \  
&& mv phpstan /usr/local/bin/phpstan  
  
COPY php.ini /usr/local/etc/php/  
COPY php.ini /usr/local/etc/php/conf.d/  
COPY www-override.conf /usr/local/etc/php-fpm.d/zzz-www-override.conf  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["php-fpm", "-F"]  

