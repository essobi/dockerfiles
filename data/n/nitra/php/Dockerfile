FROM php:7.1-fpm  
MAINTAINER Nitra  
  
ENV MEMORY_LIMIT 1024M  
ENV MAX_EXECUTION_TIME 3600  
ENV MAX_UPLOAD_SIZE 5000M  
ENV MAX_BODY_SIZE 5000M  
ENV TIME_ZONE "Europe/Kiev"  
ENV USE_COMPOSER "True"  
ENV DISPLAY_ERRORS off  
RUN apt-get update \  
&& apt-get install -y git zlib1g-dev libicu-dev g++ nodejs netcat npm
libldap2-dev libldb-dev libfreetype6-dev libjpeg62-turbo-dev libmcrypt-dev
libpng12-dev libmcrypt. \  
&& ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \  
&& docker-php-ext-install zip pdo_mysql mbstring mcrypt gd ldap intl \  
&& ln -s /usr/bin/nodejs /usr/bin/node \  
&& npm install -g bower \  
&& npm install -g uglifycss  
  
RUN pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/bin/composer  
  
RUN touch $PHP_INI_DIR/conf.d/php.ini  
RUN echo "ignore_user_abort = on" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "display_errors = $DISPLAY_ERRORS" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "memory_limit = $MEMORY_LIMIT" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "max_execution_time = $MAX_EXECUTION_TIME" >>
$PHP_INI_DIR/conf.d/php.ini  
RUN echo "upload_max_filesize = $MAX_UPLOAD_SIZE" >>
$PHP_INI_DIR/conf.d/php.ini  
RUN echo "post_max_size = $MAX_BODY_SIZE" >> $PHP_INI_DIR/conf.d/php.ini  
RUN echo "date.timezone = $TIME_ZONE" >> $PHP_INI_DIR/conf.d/php.ini  
  
ADD start.sh /start.sh  
ADD .bowerrc /root/.bowerrc  
RUN ln -snf /usr/share/zoneinfo/$TIME_ZONE /etc/localtime && echo $TIME_ZONE >
/etc/timezone  
  
WORKDIR /var/www  
CMD ["/bin/bash", "/start.sh"]

