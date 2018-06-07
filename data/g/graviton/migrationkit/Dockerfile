FROM php:7-alpine  
  
COPY . /app  
ADD src/Resources/docker/init.sh /  
  
RUN chmod a+x /init.sh && \  
apk add --no-cache tini su-exec curl git && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
cd /app && \  
composer install --optimize-autoloader --no-interaction --no-progress && \  
composer dump-autoload --optimize --no-dev --classmap-authoritative && \  
composer clear-cache  
  
ENTRYPOINT ["/sbin/tini", "--", "/init.sh", "/app/bin/migrationkit"]  

