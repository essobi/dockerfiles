FROM php:apache  
  
MAINTAINER Robert Schneider <shakemedev@gmail.com>  
  
ARG TAG=17.4  
RUN apt-get update && apt-get install --assume-yes \  
rsync \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD https://git.tt-rss.org/git/tt-rss/archive/${TAG}.tar.gz /ttr.tar.gz  
  
RUN mkdir -p /usr/src/app \  
&& tar -xzf /ttr.tar.gz -C /usr/src/app --strip 1 \  
&& chown www-data.root -R /usr/src/app \  
&& chmod 0777 \  
/usr/src/app/cache \  
/usr/src/app/feed-icons \  
/usr/src/app/lock \  
&& echo "${TAG}" > /usr/src/APP_VERSION  
  
RUN docker-php-ext-enable opcache \  
&& docker-php-ext-install -j$(nproc) mysqli  
  
RUN { \  
echo 'opcache.enable=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache.ini  
  
VOLUME /var/www/html  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  
  

