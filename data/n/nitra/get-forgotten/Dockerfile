FROM php:7  
ENV PROJECT_ROOT /var/www/get-forgotten/  
  
ENV MEMORY_LIMIT 2048M  
ENV MAX_EXECUTION_TIME 3600  
ENV MAX_UPLOAD_SIZE 5M  
ENV MAX_BODY_SIZE 10M  
ENV TIME_ZONE "Europe/Kiev"  
ENV USE_COMPOSER "True"  
ENV DISPLAY_ERRORS on  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y curl git unzip zlib1g-dev \  
&& docker-php-ext-install zip \  
&& rm -rf /var/lib/apt/lists/* \  
  
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
  
RUN mkdir -p $PROJECT_ROOT  
COPY . $PROJECT_ROOT  
WORKDIR $PROJECT_ROOT  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN composer update  
  
ENTRYPOINT ["php", "index.php"]  

