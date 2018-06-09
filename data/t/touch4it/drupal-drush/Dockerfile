FROM composer/composer:alpine  
  
RUN apk --update add \  
bash \  
build-base \  
libpq \  
mysql-client \  
postgresql-client \  
postgresql-dev \  
php7-pear \  
patch \  
tar && \  
docker-php-ext-install mysqli pgsql pdo_mysql pdo_pgsql && \  
apk del build-base postgresql-dev && \  
rm -rf /var/cache/apk/*  
  
RUN git clone \--branch="master" https://github.com/phpredis/phpredis.git
/usr/src/php/ext/redis && \  
docker-php-ext-install redis && \  
php -m && php -r "new Redis();"  
  
ENV DRUSH_VERSION 7.3.0  
RUN composer global require drush/drush:"$DRUSH_VERSION" \--prefer-dist  
  
ENTRYPOINT []  
  
CMD ["tail", "-f", "/dev/null"]  

