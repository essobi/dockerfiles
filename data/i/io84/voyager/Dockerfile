FROM io84/laravel:5.4.16-alpine  
MAINTAINER Rushairer <rushairer@163.com>  
  
ENV WEBAPP_WWW_DIR /var/www  
ARG CN_RESOURCES_CDN=false  
  
RUN apk --no-cache add libpng-dev jpeg-dev \  
&& docker-php-ext-install pdo_mysql \  
gd  
WORKDIR /usr/local/laravel  
RUN composer require "tcg/voyager:v0.11.10"  
  
COPY ./resources/voyager/resources/views/vendor
/usr/local/laravel/resources/views/vendor  
COPY ./resources/voyager/public/vendor /usr/local/laravel/public/vendor  
COPY
./resources/voyager/database/seeds/CnLocalResourcesSettingsTableSeeder.php
/usr/local/laravel/database/seeds/CnLocalResourcesSettingsTableSeeder.php  
WORKDIR $WEBAPP_WWW_DIR  
  
EXPOSE 80  
COPY ./resources/docker-voyager-entrypoint /usr/local/bin  
CMD ["docker-voyager-entrypoint"]  
  

