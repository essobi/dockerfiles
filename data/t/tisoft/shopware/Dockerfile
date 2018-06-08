FROM php:5-apache  
MAINTAINER Markus Heberling <markus@tisoft.de>  
run apt-get update && apt-get install -y wget unzip && apt-get clean  
  
RUN apt-get update && apt-get install -y zlib1g-dev libfreetype6-dev
libjpeg62-turbo-dev libpng12-dev libxml2-dev libssl-dev \  
&& apt-get clean \  
&& docker-php-ext-install -j$(nproc) zip pdo_mysql soap ftp \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install -j$(nproc) opcache \  
&& pecl install apcu-4.0.11 \  
&& docker-php-ext-enable apcu  
  
#install ioncube  
RUN mkdir /tmp/ioncube_install \  
&& cd /tmp/ioncube_install \  
&& wget
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
-O /tmp/ioncube_install/ioncube_loaders_lin_x86-64.tar.gz \  
&& tar zxvf /tmp/ioncube_install/ioncube_loaders_lin_x86-64.tar.gz \  
&& mv /tmp/ioncube_install/ioncube/ioncube_loader_lin_5.6.so `php-config
--extension-dir` \  
&& rm -rf /tmp/ioncube_install \  
&& echo "zend_extension = `php-config --extension-
dir`/ioncube_loader_lin_5.6.so">/usr/local/etc/php/conf.d/20-ioncube.ini  
  
#change some configuration for php  
RUN echo "memory_limit = 256M">/usr/local/etc/php/conf.d/30-memory.ini \  
&& echo "upload_max_filesize = 8M">/usr/local/etc/php/conf.d/30-upload.ini  
  
RUN a2enmod rewrite  
  
RUN wget
http://releases.s3.shopware.com.s3.amazonaws.com/install_5.4.1_00a0b805318ebc649726675b82db56d7bd308bd2.zip
-O /shopware.zip  
  
COPY shopware-foreground /usr/local/bin/  
CMD ["shopware-foreground"]  

