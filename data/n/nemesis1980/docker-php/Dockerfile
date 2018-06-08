FROM php:7.1.1-fpm  
  
MAINTAINER nemesis1988  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
curl \  
libmemcached-dev \  
libz-dev \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
git \  
mysql-client  
  
# Install the PHP mcrypt extention  
RUN docker-php-ext-install mcrypt  
  
# Install the PHP pdo_mysql extention  
RUN docker-php-ext-install pdo_mysql  
  
RUN apt-get purge --auto-remove -y zlib1g-dev \  
&& apt-get -y install libssl-dev libc-client2007e-dev libkrb5-dev \  
&& docker-php-ext-configure imap --with-imap-ssl --with-kerberos \  
&& docker-php-ext-install imap \  
&& docker-php-ext-install opcache  
  
#####################################  
# OpCahce  
#####################################  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
#####################################  
# ZipArchive:  
#####################################  
  
RUN docker-php-ext-install zip && \  
docker-php-ext-enable zip  
  
#####################################  
# Composer:  
#####################################  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#####################################  
# Set Timezone  
#####################################  
  
ARG TZ=UTC  
ENV TZ ${TZ}  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
ENV COMPOSER_ALLOW_SUPERUSER 1  
RUN composer global require "hirak/prestissimo:^0.3"

