FROM php:7  
ENV PROJECT_ROOT /usr/src/main  
  
ENV MEMORY_LIMIT 2048M  
ENV MAX_EXECUTION_TIME 3600  
ENV MAX_UPLOAD_SIZE 5000M  
ENV MAX_BODY_SIZE 5000M  
ENV TIME_ZONE "Europe/Kiev"  
ENV USE_COMPOSER "True"  
ENV DISPLAY_ERRORS on  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
VOLUME ["${PROJECT_ROOT}/sitespeed"]  
VOLUME ["/browsertime-results"]  
  
# INSTALL DEPENDENCIES  
RUN echo "deb http://ftp.de.debian.org/debian stretch main" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y \  
build-essential \  
automake \  
autoconf \  
libtool \  
zlib1g-dev \  
openssl \  
libpcre3 \  
libpcre3-dev \  
libcurl4-openssl-dev \  
unzip \  
wget \  
git \  
curl \  
apt-transport-https \  
mercurial \  
libssl1.0.0 \  
libssl-dev \  
libpq-dev \  
php7.0-pgsql  
  
RUN docker-php-ext-install bcmath pdo pgsql pdo_pgsql zip mbstring  
  
# REMOVE UNUSED FILES  
RUN apt-get remove -y build-essential zlib1g-dev libpcre3-dev unzip \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* -vf  
  
# PHP  
RUN touch $PHP_INI_DIR/conf.d/php.ini \  
&& echo "ignore_user_abort = on" >> $PHP_INI_DIR/conf.d/php.ini \  
&& echo "display_errors = $DISPLAY_ERRORS" >> $PHP_INI_DIR/conf.d/php.ini \  
&& echo "memory_limit = $MEMORY_LIMIT" >> $PHP_INI_DIR/conf.d/php.ini \  
&& echo "max_execution_time = $MAX_EXECUTION_TIME" >>
$PHP_INI_DIR/conf.d/php.ini \  
&& echo "upload_max_filesize = $MAX_UPLOAD_SIZE" >>
$PHP_INI_DIR/conf.d/php.ini \  
&& echo "post_max_size = $MAX_BODY_SIZE" >> $PHP_INI_DIR/conf.d/php.ini \  
&& echo "date.timezone = $TIME_ZONE" >> $PHP_INI_DIR/conf.d/php.ini  
  
RUN mkdir -p $PROJECT_ROOT/  
COPY . $PROJECT_ROOT/  
WORKDIR $PROJECT_ROOT/  
  
# COMPOSER  
RUN php -r "readfile('https://getcomposer.org/installer');" | php  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN composer install  
  
EXPOSE 80 443  
CMD ["php","crab.php"]

