FROM php:7.1-apache  
  
COPY php.ini /usr/local/etc/php/  
RUN apt-get update \  
&& apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libxml2-dev \  
git \  
&& docker-php-ext-install pdo_mysql mysqli mbstring iconv zip xml bcmath  
  
RUN apt-get -y install mc htop nodejs npm  
  
# xdebug  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
RUN echo "xdebug.remote_enable=1" >> /usr/local/etc/php/php.ini  
  
# PHP MongoDB extension  
RUN apt-get install -y libssl-dev  
RUN pecl install mongodb  
RUN echo "extension=mongodb.so" >> /usr/local/etc/php/conf.d/mongodb.ini  
  
# blackfire.io  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
  
# setup Composer  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN a2enmod rewrite  

