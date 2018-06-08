FROM php:7-apache  
  
RUN apt-get update  
RUN apt-get install -y apt-transport-https  
RUN curl https://repo.varnish-cache.org/GPG-key.txt | apt-key add - && echo
"deb https://repo.varnish-cache.org/debian/ jessie varnish-4.1" >>
/etc/apt/sources.list.d/varnish-cache.list  
RUN apt-get update && apt-get install -y varnish  
  
RUN curl https://raw.githubusercontent.com/xlight/varnish-4.0-configuration-
templates/master/default.vcl -o /etc/varnish/default.vcl  
  
## is it better to use ADD instead of RUN ?  
RUN apt-get install -y unzip  
RUN curl https://github.com/mrclay/minify/archive/master.zip -L -o min.zip &&
\  
unzip min.zip -d /root/ && mv /root/minify-master /root/min && rm min.zip  
RUN cd /root/min && curl -sS https://getcomposer.org/installer | php && php
composer.phar install --no-dev  
  
# Install modules : GD mcrypt iconv  
RUN apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
# memcached module  
RUN apt-get install -y libmemcached-dev  
RUN curl -o /root/memcached.zip https://github.com/php-memcached-dev/php-
memcached/archive/php7.zip -L  
RUN cd /root && unzip memcached.zip && rm memcached.zip && \  
cd php-memcached-php7 && \  
phpize && ./configure --enable-sasl && make && make install && \  
cd /root && rm -rf /root/php-memcached-* && \  
echo "extension=memcached.so" > /usr/local/etc/php/conf.d/memcached.ini && \  
echo "memcached.use_sasl = 1" >> /usr/local/etc/php/conf.d/memcached.ini  
  
#RUN curl -o /root/memcached.zip https://github.com/php-memcached-dev/php-
memcached/archive/2.2.0.zip -L  
# cd php-memcached-2.2.0 && \  
# install php pdo_mysql  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install bcmath  
  
# memcached module with sasl  
#RUN curl -o /root/libmemcached.tgz
https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz  
#RUN cd /root && tar zxvf libmemcached.tgz && cd libmemcached-1.0.18 && \  
# ./configure --enable-sasl && make && make install && \  
# cd /root && rm -rf /root/libmemcached*  
# add http no-cache header  
COPY prepend.php /root/  
RUN chmod 0755 /root && echo "auto_prepend_file = /root/prepend.php" >
/usr/local/etc/php/conf.d/prepend.ini  
  
# log to /var/www/log  
RUN mkdir -p /var/www/log  
RUN echo "error_log = /var/www/log/php_error.log" >
/usr/local/etc/php/conf.d/log.ini  
RUN echo "log_errors = On" >> /usr/local/etc/php/conf.d/log.ini  
RUN echo "" > /etc/apache2/conf-enabled/log.conf  
  
# enable rewrite  
RUN mv /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/  
COPY rewrite.conf /etc/apache2/conf-enabled/rewrite.conf  
  
# add check_alive.php  
echo "<?php echo 'OK'; " > /root/check_alive.php && chmod 0755 /root  
  
# add user additional conf for apache & php  
# add to CMD mkdir -p /var/www/conf/php && mkdir -p /var/www/conf/apache2 &&  
# RUN echo "" >> /usr/local/php/conf.d/additional.ini  
# RUN echo "" >> /etc/apache2/conf-enabled/additional.conf  
# add welcome page  
#COPY index.html /root/index.html  
# set system timezone & php timezone  
# @TODO  
EXPOSE 6081 80  
CMD ln -fs /var/www/html/.htaccess /etc/apache2/conf-enabled/.htaccess && ln
-fs /root/min /var/www/html/min && service varnish start && apache2-foreground  

