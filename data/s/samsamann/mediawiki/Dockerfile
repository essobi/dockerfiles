FROM php:7.0-apache  
  
MAINTAINER Samuel Ackermann <saemi.ackermann@gmail.com>  
  
ENV MEDIAWIKI_MAJOR 1.27  
ENV MEDIAWIKI_VERSION 1.27.1  
ENV MEDIAWIKI_DOWNLOAD_URL
https://releases.wikimedia.org/mediawiki/$MEDIAWIKI_MAJOR/mediawiki-$MEDIAWIKI_VERSION.tar.gz  
ENV MEDIAWIKI_PATH /var/www/html/wiki  
  
RUN set -x; \  
apt-get update && apt-get install -y \  
libicu52 \  
libicu-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng12-dev \  
libldap2-dev \  
&& rm -r /var/lib/apt/lists/*  
RUN set -x; \  
a2enmod rewrite  
RUN set -x; \  
ln -s /usr/lib/x86_64-linux-gnu/libl*.so /usr/lib \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) mbstring intl mysqli gd ldap \  
&& docker-php-ext-enable opcache  
RUN set -x; \  
curl -fO $MEDIAWIKI_DOWNLOAD_URL \  
&& mkdir wiki \  
&& tar -xzf mediawiki-$MEDIAWIKI_VERSION.tar.gz -C $MEDIAWIKI_PATH \--strip-
components=1 \  
&& rm -f mediawiki-$MEDIAWIKI_VERSION.tar.gz  
  
COPY config/apache.conf /etc/apache2/conf-enabled/wiki.conf  
COPY config/LocalSettings.php $MEDIAWIKI_PATH/LocalSettings.php  
COPY ./docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

