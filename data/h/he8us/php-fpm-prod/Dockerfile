FROM he8us/php-fpm-common:7.1  
  
MAINTAINER Cedric Michaux <cedric@he8us.be>  
  
ENV APCU_VERSION 5.1.8  
ENV APCU_BC_VERSION 1.0.3  
  
RUN \  
apk --no-cache add \  
\--virtual .phpize-deps \  
build-base \  
autoconf \  
&& pecl install apcu-$APCU_VERSION \  
&& pecl install apcu_bc-$APCU_BC_VERSION \  
&& docker-php-ext-enable apcu --ini-name 10-docker-php-ext-apcu.ini \  
&& docker-php-ext-enable apc --ini-name 20-docker-php-ext-bc-apc.ini \  
&& apk del .phpize-deps  

