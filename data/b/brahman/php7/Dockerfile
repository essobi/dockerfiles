FROM php:7.0-fpm  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
mailutils ssmtp \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd mbstring zip opcache\  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install pdo_mysql  
  
# modify ssmtp settings  
RUN sed -ri -e 's/^(mailhub=).*/\1smtp-server/' -e
's/^#(FromLineOverride)/\1/' /etc/ssmtp/ssmtp.conf  
RUN echo 'sendmail_path = "/usr/sbin/ssmtp -t"' >
/usr/local/etc/php/conf.d/mail.ini

