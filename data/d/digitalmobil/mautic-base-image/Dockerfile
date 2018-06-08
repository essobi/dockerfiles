FROM php:5.6-apache  
  
MAINTAINER {klaus.hartl,roland.tuschl}@digitalmobil.com  
  
# Enable Apache Rewrite Module  
RUN a2enmod rewrite  
  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \  
libc-client-dev libfreetype6-dev libicu-dev libjpeg-dev libkrb5-dev libmcrypt-
dev libpng-dev libssl-dev libwebp-dev libxpm-dev unzip zip \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN docker-php-ext-configure imap --with-imap --with-imap-ssl --with-kerberos  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
  
RUN docker-php-ext-install gd imap intl mbstring mcrypt mysqli pdo pdo_mysql
zip  
  
RUN { \  
echo 'date.timezone = "Europe/Berlin"'; \  
echo 'upload_max_filesize = 20M'; \  
echo 'post_max_size = 20M'; \  
echo 'memory_limit = 512M'; \  
} > /usr/local/etc/php/conf.d/mautic.ini  
  
RUN apt-get update && apt-get install -y --force-yes --no-install-recommends \  
cron \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN sed -i -E 's/(session\s*required\s*pam_loginuid.so)/#\1/' /etc/pam.d/cron  
  
CMD ["apache2-foreground"]  

