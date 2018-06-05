FROM php:5.6-apache  
  
RUN a2enmod rewrite expires  
  
# install the PHP extensions  
RUN apt-get update && apt-get upgrade -y && apt-get install -y libpng12-dev
libjpeg-dev cron vim \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd mysql mysqli opcache mbstring \  
&& apt-get autoremove \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# set recommended PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=0'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
# set xdebug  
# see https://gist.github.com/chadrien/c90927ec2d160ffea9c4  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
# set extra PHP.ini settings  
RUN { \  
echo 'date.timezone="Asia/Tokyo"'; \  
echo 'log_errors=On'; \  
echo 'memory_limit=-1'; \  
echo 'max_execution_time=0'; \  
echo 'post_max_size=0'; \  
echo 'upload_max_filesize=2048G'; \  
} > /usr/local/etc/php/conf.d/php-extra.ini  
  
# replace ErrorLog to CommonLog  
RUN sed -i -e"s/CustomLog/#CustomLog/" /etc/apache2/apache2.conf \  
&& sed -i -e"s/ErrorLog \/proc\/self\/fd\/2/ErrorLog \/proc\/self\/fd\/1/"
/etc/apache2/apache2.conf  
  
# fix permission for osx  
RUN usermod -u 1000 www-data \  
&& usermod -G staff www-data  
  
VOLUME /var/www/html  
  
ENV TZ JST-9  
ENV XDEBUG_CONFIG remote_host=  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

