FROM php:7.1-apache  
  
RUN apt-get update && apt-get install -y \  
bzip2 \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libicu-dev \  
libjpeg-dev \  
libldap2-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxml2-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
#
https://docs.nextcloud.com/server/9/admin_manual/installation/source_installation.html  
RUN docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \  
&& docker-php-ext-install gd exif intl mbstring mcrypt ldap pdo_mysql zip  
  
RUN a2enmod rewrite  
  
ENV NEXTCLOUD_VERSION 11.0.3  
  
RUN curl -fsSL -o nextcloud-${NEXTCLOUD_VERSION}.tar.bz2 \  
"https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2"
\  
&& curl -fsSL -o nextcloud-${NEXTCLOUD_VERSION}.tar.bz2.sha256 \  
"https://download.nextcloud.com/server/releases/nextcloud-${NEXTCLOUD_VERSION}.tar.bz2.sha256"
\  
&& sha256sum -c nextcloud-${NEXTCLOUD_VERSION}.tar.bz2.sha256 \  
&& tar -xjf nextcloud-${NEXTCLOUD_VERSION}.tar.bz2 -C /usr/src \  
&& rm -rf /var/www/html \  
&& mv /usr/src/nextcloud /var/www/html \  
&& mkdir -p /var/www/html/data \  
&& chown -R www-data /var/www/html  

