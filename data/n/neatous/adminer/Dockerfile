FROM php:7.2-alpine  
  
STOPSIGNAL SIGINT  
  
RUN addgroup -S adminer \  
&& adduser -S -G adminer adminer \  
&& mkdir -p /var/www/html \  
&& chown -R adminer:adminer /var/www/html  
  
WORKDIR /var/www/html  
  
RUN apk add --no-cache git libpq  
  
RUN set -x \  
&& apk add --no-cache --virtual .build-deps \  
postgresql-dev \  
sqlite-dev \  
&& docker-php-ext-install pdo_mysql pdo_pgsql pdo_sqlite \  
&& apk del .build-deps  
  
RUN set -x \  
&& cd /tmp \  
&& git clone -b master --single-branch https://github.com/vrana/adminer.git \  
&& cd /tmp/adminer/ \  
&& php /tmp/adminer/compile.php \  
&& mv /tmp/adminer/adminer.php /var/www/html/index.php \  
&& rm -rf /tmp/adminer  
  
USER adminer  
CMD [ "php", "-S", "[::]:8080", "-t", "/var/www/html" ]  
  
EXPOSE 8080  

