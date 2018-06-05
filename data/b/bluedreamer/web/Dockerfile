FROM php:7.1-apache  
RUN apt-get update -y \  
&& apt-get install -y libssh2-1 libssh2-1-dev vim \  
&& pecl install xdebug-2.5.0 \  
&& pecl install ssh2-alpha \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-enable ssh2 \  
&& docker-php-ext-enable xdebug \  
&& echo -e
"xdebug.remote_port=9000\nxdebug.remote_enable=1\nxdebug.remote_connect_back=1\n"
>> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  

