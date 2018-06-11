FROM php:7.1-cli-alpine  
  
MAINTAINER Ferri Sutanto <greenhouseprod@gmail.com>  
  
RUN set -x; \  
\  
apk add --no-cache \  
git \  
unzip \  
zip \  
; \  
php -r "readfile('http://getcomposer.org/installer');" \  
| php -- --install-dir=/usr/local/bin/ \--filename=composer; \  
\  
mkdir -p /.composer; \  
chmod -R ugo+rw /.composer;  
  
  

