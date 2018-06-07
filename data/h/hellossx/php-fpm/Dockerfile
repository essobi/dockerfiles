FROM php:fpm  
  
MAINTAINER Scott Wilcox <scott@dor.ky>  
  
# exit if a command fails  
RUN set -e  
  
# Stop upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
ENV DEBIAN_FRONTEND noninteractive  
  
# Dependancies for extensions  
RUN apt-get update -yqq  
RUN apt-get install  
RUN apt-get update && apt-get install -y \  
libicu-dev \  
libpng-dev \  
libjpeg-dev \  
libbz2-dev \  
libpq-dev \  
libmemcached-dev \  
libmcrypt-dev \  
libfreetype6 \  
libjpeg62-turbo \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libpng12-0 \  
libsqlite3-dev \  
libjpeg-dev \  
libmcrypt4 \  
libpng3 \  
libpng++-dev \  
libgd-dev  
  
# Install extensions  
RUN docker-php-ext-install pdo pdo_mysql mcrypt mysqli pdo_sqlite intl bz2
pcntl  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib/x86_64-linux-gnu \  
\--with-png-dir=/usr/lib/x86_64-linux-gnu \  
\--with-freetype-dir=/usr/lib/x86_64-linux-gnu \  
&& docker-php-ext-install gd  
  
# Installer composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer && chmod +x /usr/local/bin/composer  
  
# Cleanup  
RUN apt-get remove --purge -y curl build-essential && apt-get autoclean &&
apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 9000  
WORKDIR /www  
  
CMD ["php-fpm"]  

