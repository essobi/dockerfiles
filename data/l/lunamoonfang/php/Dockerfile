FROM php:7.1-fpm  
  
MAINTAINER Thomas Wiringa <thomas@tjwiringa.nl>  
  
RUN apt-get update && apt-get install libpq-dev libmcrypt-dev libpng-dev
libjpeg62-turbo-dev -y --no-install-recommends  
  
# Install extensions using the helper script provided by the base image  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib/x86_64-linux-gnu \  
\--with-png-dir=/usr/lib/x86_64-linux-gnu \  
&& docker-php-ext-install \  
pdo_mysql \  
fileinfo \  
gd \  
tokenizer  
  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
  
RUN usermod -u 1000 www-data  
  
ADD ./php.ini /usr/local/etc/php/conf.d  
ADD ./php.pool.conf /usr/local/etc/php-fpm.d/  
  
WORKDIR /var/www/html  
  
USER www-data  

