# See https://github.com/lomadi/app-webtrees/tree/master/images/webtrees  
FROM php:5.6-apache  
MAINTAINER lomadi <lomadi@mac.com>  
  
RUN apt-get update && apt-get install -y wget unzip libfreetype6
libjpeg62-turbo libmcrypt4 libpng12-0 sendmail --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
RUN buildDeps=" \  
libfreetype6-dev \  
libjpeg-dev \  
libldap2-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
"; \  
set -x \  
&& apt-get update && apt-get install -y $buildDeps \--no-install-recommends &&
rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --enable-gd-native-ttf --with-jpeg-
dir=/usr/lib/x86_64-linux-gnu --with-png-dir=/usr/lib/x86_64-linux-gnu --with-
freetype-dir=/usr/lib/x86_64-linux-gnu \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install mysql \  
&& docker-php-ext-install mysqli \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install zip \  
&& apt-get purge -y --auto-remove $buildDeps  
  
WORKDIR /var/www/html/  
RUN wget https://launchpad.net/webtrees/1.7/1.7.8/+download/webtrees-1.7.8.zip  
RUN unzip webtrees-*.zip  
RUN chown -R www-data:www-data /var/www/html  
RUN rm webtrees-*.zip  
  
ADD scripts /opt/scripts  
WORKDIR /opt/scripts  
RUN chmod a+x *.sh  
  
ADD config/php.ini /usr/local/etc/php  
  
ENTRYPOINT ["/opt/scripts/entrypoint.sh"]

