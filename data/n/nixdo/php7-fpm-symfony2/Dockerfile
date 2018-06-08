FROM php:7.0.6-fpm  
  
RUN apt-get update  
RUN apt-get install -y git  
RUN apt-get install -y zlib1g-dev  
RUN apt-get install -y nodejs && ln -s /usr/bin/nodejs /usr/bin/node  
RUN apt-get install -y libicu-dev  
RUN docker-php-ext-install zip pdo_mysql intl  
RUN apt-get install -y ghostscript  
RUN apt-get install -y ufraw  
RUN apt-get install -y poppler-utils  
RUN apt-get install -y libmagickwand-dev  
RUN apt-get install -y imagemagick  
RUN apt-get install -y p7zip-full  
RUN pecl install imagick-3.4.2  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/bin/composer  
  
ENV MEMORY_LIMIT -1  
ENV MAX_EXECUTION_TIME 3200  
ENV MAX_UPLOAD_SIZE 5000M  
ENV MAX_BODY_SIZE 5000M  
  
RUN touch $PHP_INI_DIR/conf.d/php.ini  
RUN echo "extension=imagick.so" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "ignore_user_abort = on" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "display_errors = off" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "memory_limit = $MEMORY_LIMIT" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "max_execution_time = $MAX_EXECUTION_TIME" >>
$PHP_INI_DIR/conf.d/php.ini  
RUN echo "upload_max_filesize = $MAX_UPLOAD_SIZE" >>
$PHP_INI_DIR/conf.d/php.ini  
RUN echo "post_max_size = $MAX_BODY_SIZE" >> $PHP_INI_DIR/conf.d/php.ini  
  
RUN echo "display_errors = off" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "display_startup_errors = off" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "error_reporting = E_ALL" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "log_errors = on" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "ignore_repeated_errors = Off" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "report_memleaks = On" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "track_errors = On" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "error_log = /dev/stderr" >> $PHP_INI_DIR/conf.d/php.ini  
  
RUN ln -sf /dev/stdout /var/log/access.log && ln -sf /dev/stderr
/var/log/error.log  
  
ADD start.sh /var/app/start.sh  
WORKDIR /var/app  
CMD ["/bin/bash", "start.sh"]  

