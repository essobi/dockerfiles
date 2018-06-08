FROM timonier/php:fpm  
  
MAINTAINER Morgan Auchede <morgan.auchede@gmail.com>  
  
ENV \  
PHPCI_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress \  
nginx \  
\  
# Install block8/phpci  
\  
&& mkdir -p /opt \  
&& git clone "https://github.com/Block8/PHPCI" /opt/phpci \  
&& composer install --no-dev --optimize-autoloader --working-dir /opt/phpci \  
&& chown -R www-data:www-data /opt/phpci \  
\  
# Clean  
\  
&& rm -f -r \  
/opt/phpci/.git \  
/opt/phpci/PHPCI/build \  
/root/.composer \  
/tmp/*  
  
COPY ./rootfs /  

