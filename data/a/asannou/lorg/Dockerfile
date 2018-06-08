FROM php:5-alpine  
  
WORKDIR /root  
  
RUN apk --no-cache add libjpeg-turbo libvpx libpng freetype \  
&& apk --no-cache --virtual .build-dependencies add libjpeg-turbo-dev libvpx-
dev libpng-dev freetype-dev \  
&& docker-php-ext-configure gd --with-jpeg-dir=/usr/include/ --with-vpx-
dir=/usr/include/ --with-freetype-dir=/usr/include/ \  
&& docker-php-ext-install pcntl gd \  
&& apk del .build-dependencies  
  
COPY php.ini /usr/local/etc/php/  
  
RUN apk --no-cache --virtual .build-dependencies add git \  
&& git clone https://github.com/jensvoid/lorg.git /usr/src/lorg \  
&& apk del .build-dependencies  
  
RUN sed -i -E "s/(static \\\$phpids_path =
')[^']+/\1\/usr\/src\/lorg\/phpids\//g" /usr/src/lorg/lorg \  
&& sed -i -E "s/(static \\\$geoip_path =
')[^']+/\1\/usr\/src\/lorg\/geoip\//g" /usr/src/lorg/lorg \  
&& sed -i -E "s/(static \\\$pchart_path =
')[^']+/\1\/usr\/src\/lorg\/pchart\//g" /usr/src/lorg/lorg  
  
ENTRYPOINT ["/usr/src/lorg/lorg"]  

