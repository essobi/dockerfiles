FROM php:7.1-fpm  
  
ENV SCRM_VERSION v7.10.5  
# Install requirements  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get \  
install -y --no-install-recommends \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libcurl4-openssl-dev \  
libssl-dev \  
libpng-dev \  
libpq-dev \  
libxml2-dev \  
zlib1g-dev \  
libc-client-dev \  
libkrb5-dev \  
libldap2-dev \  
cron \  
git \  
busybox-static  
  
# Docker image configuration  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-configure imap --with-kerberos --with-imap-ssl \  
&& docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ \  
&& docker-php-ext-install -j$(nproc) iconv \  
mcrypt \  
pdo_mysql \  
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
  
WORKDIR /var/www/html  
  
#Setting UP SuiteCRM  
RUN curl
https://codeload.github.com/salesagility/SuiteCRM/tar.gz/${SCRM_VERSION} | tar
xzv --strip 1  
  
#Setting Up config file redirect for proper use with docker volumes  
RUN mkdir conf.d \  
&& touch conf.d/config.php conf.d/config_override.php \  
&& ln -s conf.d/config.php \  
&& ln -s conf.d/config_override.php  
  
# composer  
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');"  
RUN php /tmp/composer-setup.php --install-dir=/usr/local/bin
--filename=composer  
RUN composer install --no-plugins --no-scripts  
  
# Adding crontab for www-data user  
RUN mkdir -p /var/spool/cron/crontabs; \  
echo '* * * * * php -f /var/www/html/cron.php' > /var/spool/cron/crontabs/www-
data  
  
# bootstrap files  
COPY php.custom.ini /usr/local/etc/php/conf.d/  
COPY ./bootstrap /bootstrap  
  
# clean temporary files and packages  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME [ "/var/www/html/upload", "/var/www/html/conf.d" ]  
  
EXPOSE 80  
ENTRYPOINT ["/bootstrap/suitecrm-init.sh"]  
CMD ["php-fpm"]  

