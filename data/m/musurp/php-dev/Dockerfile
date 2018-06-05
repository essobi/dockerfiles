FROM musurp/php:7.0.26-cli  
  
RUN apt-get update -y \  
&& apt-get install -y \  
libicu-dev \  
libmcrypt-dev \  
libpq-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& pecl install -o -f xdebug \  
&& rm -rf /tmp/pear \  
&& echo "zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20151012/xdebug.so" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_host=10.0.2.2" >> /usr/local/etc/php/conf.d/xdebug.ini
\  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini
\  
&& echo "xdebug.remote_connect_back=On" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.idekey=PHPSTORM" >> /usr/local/etc/php/conf.d/xdebug.ini  

