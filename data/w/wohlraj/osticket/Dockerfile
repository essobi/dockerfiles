FROM php:5.6-apache  
  
# PHP ZipArchive, mbstring  
RUN apt-get update \  
&& apt-get install -y zlib1g-dev libldap2-dev libpcre3-dev \  
&& docker-php-ext-install mbstring zip > /dev/null  
# Install PDO MySQL driver  
# See https://github.com/docker-library/php/issues/62  
RUN docker-php-ext-install pdo mysql > /dev/null \  
&& docker-php-ext-install pdo mysqli > /dev/null  
# LDAP  
RUN docker-php-ext-configure ldap \--with-libdir=lib/x86_64-linux-gnu/ >
/dev/null \  
&& docker-php-ext-install ldap > /dev/null  
# Enable Apache mod_rewrite  
RUN a2enmod rewrite \  
&& echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Installation osticket-specific extensions  
RUN apt-get update && apt-get install -y libicu-dev g++ \  
&& docker-php-ext-configure intl > /dev/null \  
&& docker-php-ext-install intl > /dev/null  
RUN apt-get update && apt-get install -y libpng-dev \  
&& docker-php-ext-install gd > /dev/null  
RUN pecl install apcu-4.0.10 > /dev/null \  
&& docker-php-ext-enable apcu > /dev/null  
RUN docker-php-ext-configure opcache --enable-opcache > /dev/null \  
&& docker-php-ext-install opcache > /dev/null  
# Setting timezone, max upload size  
RUN echo "date.timezone = Europe/Paris" >> /usr/local/etc/php/conf.d/docker-
php-ext-timezone.ini  
RUN echo "upload_max_filesize = 100M" >> /usr/local/etc/php/conf.d/docker-php-
ext-uploadsize.ini  
RUN echo "post_max_size = 100M" >> /usr/local/etc/php/conf.d/docker-php-ext-
uploadsize.ini  
  
# Enabling crontab  
COPY cron/crontab /var/spool/crontabs/root  
RUN apt-get update && apt-get install -y cron \  
&& crontab /var/spool/crontabs/root  
  
# Copying code into image  
ADD . /var/www/html  
  
RUN rm -rf /var/www/html/setup  
  
CMD /etc/init.d/cron start && apache2-foreground

