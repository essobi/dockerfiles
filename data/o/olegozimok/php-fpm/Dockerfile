FROM olegozimok/php-fpm:5.5-full  
  
MAINTAINER Oleg Ozimok "ozimok.oleg@gmail.com"  
RUN curl -L -o /tmp/xdebug.gz https://pecl.php.net/get/xdebug-2.3.3.tgz \  
&& tar xfz /tmp/xdebug.gz \  
&& rm -r /tmp/xdebug.gz \  
&& mv xdebug-2.3.3 /usr/src/php/ext/xdebug \  
&& docker-php-ext-install xdebug  
  
COPY php.ini /usr/local/etc/php/  
  
EXPOSE 9001  

