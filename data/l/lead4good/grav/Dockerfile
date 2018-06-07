FROM php:fpm-alpine  
  
ENV GRAV_DOWNLOAD_SHA256
c7cc861bc4838f3a5880d85791277c67b28dfbe8676e6e5d8fe323a960c6eb82  
  
RUN mkdir -p /usr/src/grav \  
&& curl -fSL -o /usr/src/grav/grav-admin.zip \  
'https://github.com/getgrav/grav/releases/download/1.2.4/grav-
admin-v1.2.4.zip' \  
&& echo "$GRAV_DOWNLOAD_SHA256 /usr/src/grav/grav-admin.zip" | sha256sum -c -  
  
RUN set -xe \  
&& apk --no-cache add libpng \  
&& apk --no-cache add --virtual .build-deps libpng-dev unzip \  
&& docker-php-ext-install gd zip \  
&& ln -s /usr/src/grav /usr/src/grav/grav-admin \  
&& unzip /usr/src/grav/grav-admin.zip -d /usr/src/grav \  
&& rm /usr/src/grav/grav-admin.zip /usr/src/grav/grav-admin \  
&& chown -R www-data:www-data /usr/src/grav \  
&& apk del .build-deps  
  
COPY ./docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT [ "/bin/sh", "/entrypoint.sh" ]  
CMD [ "php-fpm" ]  

