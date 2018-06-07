FROM php:7.2-alpine  
  
ADD / /graviton-import-export/  
  
RUN apk update && \  
apk upgrade && \  
# deps for building  
apk add \--update git bash curl autoconf build-base openssl-dev libmcrypt-dev
icu-dev pcre-dev zlib-dev bzip2-dev && \  
docker-php-ext-install bcmath zip bz2 ctype && \  
pecl install mongodb && \  
docker-php-ext-enable mongodb && \  
adduser www-data root && \  
apk del \--purge autoconf build-base && \  
# install app  
curl -sS https://getcomposer.org/installer | php \-- --install-
dir=/usr/local/bin --filename=composer && \  
cd /graviton-import-export && \  
composer install \--no-dev --no-interaction --no-progress && \  
composer dump-autoload \--optimize --no-dev --classmap-authoritative && \  
composer clear-cache && \  
# cleanup  
pecl clear-cache && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/pear/  
  
USER www-data  
  
CMD ["php", "/graviton-import-export/bin/graviton-import-export"]  

