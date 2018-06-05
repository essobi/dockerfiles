# limesurvey installation  
#  
# VERSION 1.0  
#  
FROM php:7.0-apache  
MAINTAINER Lukas Pessl  
  
ENV LIMESURVEY_VERSION=2.63.1  
ENV VERSION_CODE=170305  
RUN echo 'deb http://packages.dotdeb.org jessie all' >
/etc/apt/sources.list.d/dotdeb.list && \  
curl http://www.dotdeb.org/dotdeb.gpg | apt-key add -  
  
RUN apt-get update && \  
apt-get -q -y install \  
libldap2-dev \  
libpng12-dev \  
imagemagick \  
libmcrypt-dev \  
libzip-dev \  
curl \  
php7.0-gd \  
php7.0-json \  
php7.0-ldap \  
php7.0-imap \  
php7.0-mbstring \  
php7.0-mysql \  
php7.0-xml \  
php7.0-xsl \  
php7.0-zip \  
php7.0-soap \  
mysql-client \  
libmysqlclient-dev \  
libc-client-dev \  
libkrb5-dev \  
sendmail \  
&& rm -r /var/lib/apt/lists/*  
  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/  
RUN docker-php-ext-configure imap --with-kerberos --with-imap-ssl  
  
RUN docker-php-ext-install \  
gd \  
mysqli \  
pdo_mysql \  
ldap \  
zip \  
imap  
  
RUN a2enmod php7 && a2enmod rewrite  
  
RUN curl -L
https://github.com/LimeSurvey/LimeSurvey/archive/$LIMESURVEY_VERSION+$VERSION_CODE.tar.gz
> LimeSurvey-$LIMESURVEY_VERSION-$VERSION_CODE.tar.gz  
  
RUN tar xvzf LimeSurvey-$LIMESURVEY_VERSION-$VERSION_CODE.tar.gz --directory
/var/www  
  
RUN mv /var/www/LimeSurvey-$LIMESURVEY_VERSION-$VERSION_CODE/* /var/www/html  
  
RUN chown -R www-data:www-data /var/www/html/  
  
RUN chmod -R 755 /var/www/html/tmp  
RUN chmod -R 755 /var/www/html/upload  
RUN chmod -R 775 /var/www/html/application/config  
  
RUN apt-get update && apt-get install -y libmagickwand-6.q16-dev --no-install-
recommends \  
&& ln -s /usr/lib/x86_64-linux-gnu/ImageMagick-6.8.9/bin-Q16/MagickWand-config
/usr/bin \  
&& pecl install imagick \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini  

