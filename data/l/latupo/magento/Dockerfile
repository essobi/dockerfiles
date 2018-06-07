FROM php:5.6-apache  
  
MAINTAINER Kristof Lünenschloß <kl@latupo.com>  
  
ENV MAGENTO_VERSION 1.9.1.1  
RUN curl -o magento.tar.gz -SL https://codeload.github.com/OpenMage/magento-
mirror/tar.gz/${MAGENTO_VERSION} \  
&& tar -xzf magento.tar.gz -C /usr/src/ \  
&& mv /usr/src/magento-mirror-${MAGENTO_VERSION} /usr/src/magento \  
&& rm magento.tar.gz \  
&& chown -R www-data:www-data /usr/src/magento  
  
RUN apt-get update && apt-get install -y \  
mysql-client \  
php5-mysql \  
php5-gd \  
libpng12-dev \  
libxml2-dev \  
libmcrypt-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
xmlstarlet \  
jq \  
libapache2-mod-evasive \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install pdo_mysql gd soap mcrypt mbstring  
  
RUN a2enmod rewrite && a2enmod ssl && a2enmod evasive  
  
COPY config/ /config/  
COPY scripts/create-patches.sh /usr/local/bin/create-patches  
COPY scripts/backup-databases.sh /usr/local/bin/backup-databases  
  
RUN usermod -u 1000 www-data  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  
  

