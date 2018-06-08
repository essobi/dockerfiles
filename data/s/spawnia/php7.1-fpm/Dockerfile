FROM spawnia/php7.1-fpm  
LABEL maintainer="Benedikt Franke <benedikt@franke.tech>"  
  
# Add user same as the host os user  
RUN set -x \  
&& adduser -u 1000 -D -S -G www-data me  
  
RUN apk --update --no-cache add \  
curl \  
git \  
php7 \  
php7-zlib \  
php7-phar \  
php7-pdo_sqlite \  
php7-dom \  
php7-xml \  
php7-xmlwriter \  
php7-curl \  
&& rm -rf /var/cache/apk/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
RUN composer global require hirak/prestissimo  

