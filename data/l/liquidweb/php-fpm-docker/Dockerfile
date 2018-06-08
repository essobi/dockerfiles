############################################################  
# Dockerfile to run the php-fpm process for WordPress  
############################################################  
FROM php:5-fpm  
  
# File Author / Maintainer  
MAINTAINER Banzai <rd-banzai@liquidweb.com>  
  
# Set the base image  
RUN apt-get update && apt-get install -y php5-dev  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libmhash-dev \  
libbz2-dev \  
libxml2-dev \  
ssmtp \  
zend-framework \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
RUN apt-get update && apt-get install -y libmysqlclient-dev \  
&& docker-php-ext-install mysql  
  
RUN apt-get update && apt-get install -y libmemcached-dev  
  
RUN pecl install memcache memcached \  
&& docker-php-ext-enable --ini-name memcache.ini memcache  
  
RUN docker-php-ext-install -j$(nproc) bcmath  
RUN docker-php-ext-install -j$(nproc) bz2  
RUN docker-php-ext-install -j$(nproc) calendar  
RUN docker-php-ext-install -j$(nproc) dba  
RUN docker-php-ext-install -j$(nproc) exif  
RUN docker-php-ext-install -j$(nproc) ftp  
RUN docker-php-ext-install -j$(nproc) gettext  
RUN docker-php-ext-install -j$(nproc) pcntl  
RUN docker-php-ext-install -j$(nproc) shmop  
RUN docker-php-ext-install -j$(nproc) soap  
RUN docker-php-ext-install -j$(nproc) sockets  
RUN docker-php-ext-install -j$(nproc) sysvmsg  
RUN docker-php-ext-install -j$(nproc) sysvsem  
RUN docker-php-ext-install -j$(nproc) sysvshm  
RUN docker-php-ext-install -j$(nproc) wddx  
RUN docker-php-ext-install -j$(nproc) zip  
RUN docker-php-ext-install -j$(nproc) opcache  
RUN docker-php-ext-install -j$(nproc) pdo_mysql  
RUN docker-php-ext-install -j$(nproc) mysqli  
  
RUN pecl install xdebug && docker-php-ext-enable xdebug  
  
RUN apt-get install -y imagemagick libmagickwand-dev  
  
RUN pecl install imagick && docker-php-ext-enable imagick  
  
# Install ioncube  
# COPY files/ioncube_loaders_lin_x86-64.tar.bz2
/tmp/ioncube_loaders_lin_x86-64.tar.bz2  
ADD
https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
/tmp/  
RUN tar xvzfC /tmp/ioncube_loaders_lin_x86-64.tar.gz /tmp/ \  
&& rm /tmp/ioncube_loaders_lin_x86-64.tar.gz \  
&& mkdir -p /usr/local/ioncube \  
&& cp /tmp/ioncube/ioncube_loader_lin_5.6.so /usr/local/ioncube \  
&& rm -rf /tmp/ioncube  
COPY config/php5-ioncube.ini /usr/local/etc/php/conf.d/00-ioncube.ini  
COPY config/php5-ioncube.ini /usr/local/etc/php/cli/conf.d/00-ioncube.ini  
  
ADD run.sh /run.sh  
  
COPY config/max_upload_size.ini /usr/local/etc/php/conf.d/  
COPY config/sendmail_path.ini /usr/local/etc/php/conf.d/  
COPY config/max_execution_time.ini /usr/local/etc/php/conf.d/  
COPY config/www.conf /usr/local/etc/php-fpm.d/zz-mwp-www.conf  
COPY config/ssmtp.conf /etc/ssmtp/  
  
CMD ["/run.sh"]  

