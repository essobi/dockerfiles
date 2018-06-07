FROM php:5-alpine  
  
WORKDIR /home/www-data  
  
# Add files  
ADD app.tar.gz /home/www-data/  
COPY cjw* /usr/bin/  
COPY crontab /var/spool/cron/crontabs/root  
  
# Add packages  
RUN chmod a+x /usr/bin/cjw* \  
&& apk add \--no-cache --virtual .build-deps $PHPIZE_DEPS tzdata sqlite-dev \  
# Setup timezone  
&& cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo "Asia/Shanghai" > /etc/timezone \  
# Install PHP extensions  
&& pecl install dbase-5.1.0 \  
&& pecl bundle -d /usr/src/php/ext yaf-2.3.5 \  
&& docker-php-ext-install bcmath pdo_sqlite yaf \  
&& docker-php-ext-enable dbase \  
# Clear cache  
&& pecl clear-cache \  
&& rm -rf /tmp/pear \  
&& docker-php-source delete \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
CMD ["crond", "-f"]

