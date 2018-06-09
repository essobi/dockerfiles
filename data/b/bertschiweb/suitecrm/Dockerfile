FROM php:7-apache  
MAINTAINER Simon Hugentobler <simon.hugentobler@bertschi.com>  
  
  
  
COPY php.custom.ini /usr/local/etc/php/conf.d/  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libcurl4-openssl-dev \  
libssl-dev \  
libpng12-dev \  
libpq-dev \  
libxml2-dev \  
zlib1g-dev \  
libc-client-dev \  
libkrb5-dev \  
libldap2-dev \  
cron  
RUN docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install -j$(nproc) pdo_mysql \  
curl \  
mbstring \  
mysqli \  
zip \  
ftp \  
pdo_pgsql \  
gd \  
fileinfo \  
soap \  
zip \  
imap \  
ldap  
  
#Setting UP SuiteCRM  
RUN curl -O https://codeload.github.com/salesagility/SuiteCRM/tar.gz/v7.9.4 &&
tar xvfz v7.9.4 --strip 1 -C /var/www/html  
RUN chown www-data:www-data /var/www/html/ -R  
RUN cd /var/www/html && chmod -R 755 .  
RUN (crontab -l 2>/dev/null; echo "* * * * * cd /var/www/html; php -f cron.php
> /dev/null 2>&1 ") | crontab -  
  
#Setting Up config file redirect for proper use with docker volumes  
RUN cd /var/www/html \  
&& mkdir conf.d \  
&& mv config_override.php conf.d/ \  
&& touch /var/www/html/conf.d/config.php \  
&& ln -s /var/www/html/conf.d/config.php config.php \  
&& ln -s /var/www/html/conf.d/config_override.php config_override.php  
  
#Fix php warnings in dashboards  
RUN cd /var/www/html \  
&& sed -i.back
s/'<?php/<?php\n\nini_set\\(display_errors\,0\\)\;\nerror_reporting\\(E_ALL\
\^\ E_STRICT\\)\;\n\n/g'
/var/www/html/modules/Calls/Dashlets/MyCallsDashlet/MyCallsDashlet.php  
  
RUN apt-get clean  
  
VOLUME /var/www/html/upload  
VOLUME /var/www/html/conf.d  
  
WORKDIR /var/www/html  
EXPOSE 80  

