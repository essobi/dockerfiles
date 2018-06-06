FROM ubuntu:12.04  
# install the PHP extensions  
RUN apt-get update && apt-get upgrade -y && apt-get install -y \  
libpng12-dev libjpeg-dev cron supervisor vim libmagickwand-dev libmagickcore-
dev imagemagick unzip \  
apache2 php5-dev libapache2-mod-php5 php5-gd php5-mysql php5-imagick php-pear
\  
&& apt-get autoremove \  
&& apt-get autoclean \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# set xdebug  
RUN yes | pecl install xdebug-2.2.7 \  
&& echo "zend_extension=$(find /usr/lib/php5/ -name xdebug.so)" >
/etc/php5/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /etc/php5/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /etc/php5/conf.d/xdebug.ini \  
&& echo "xdebug.profiler_enable_trigger=1" >> /etc/php5/conf.d/xdebug.ini \  
&& echo "xdebug.profiler_enable=0" >> /etc/php5/conf.d/xdebug.ini \  
&& echo "xdebug.profiler_append=0" >> /etc/php5/conf.d/xdebug.ini \  
&& echo "xdebug.profiler_output_dir=\"/var/www\"" >>
/etc/php5/conf.d/xdebug.ini  
  
RUN yes | pecl install apc \  
&& echo "extension=$(find /usr/lib/php5/ -name apc.so)" >
/etc/php5/conf.d/apc.ini  
  
## set extra PHP.ini settings  
RUN { \  
echo 'date.timezone="Asia/Tokyo"'; \  
echo 'log_errors=On'; \  
echo 'memory_limit=-1'; \  
echo 'max_execution_time=0'; \  
echo 'post_max_size=0'; \  
echo 'upload_max_filesize=2048G'; \  
} > /etc/php5/conf.d/php-extra.ini  
  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY apache2-foreground /usr/local/bin/apache2-foreground  
RUN chmod +x /usr/local/bin/apache2-foreground  
  
# fix permission for osx  
RUN usermod -u 1000 www-data \  
&& usermod -G staff www-data  
  
RUN a2enmod rewrite expires  
  
VOLUME /var/www  
  
ENV TZ JST-9  
ENV XDEBUG_CONFIG remote_host=  
ENV CONCRETE5_VERSION 5.5.2.1  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/local/bin/apache2-foreground"]

