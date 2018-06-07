FROM richarvey/nginx-php-fpm:1.3.10  
  
RUN \  
apk add \--no-cache postgresql \  
&& apk add \--no-cache --virtual .postgres-deps postgresql-dev \  
&& docker-php-ext-install pdo_pgsql \  
&& apk del .postgres-deps  
  
RUN \  
apk add \--no-cache --virtual .build-deps autoconf g++ make \  
&& pecl install redis \  
&& docker-php-ext-enable redis \  
&& apk del .build-deps  

