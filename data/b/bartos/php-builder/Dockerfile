FROM php:alpine  
MAINTAINER Vojtech Bartos <barvoj@seznam.cz>  
  
# Configure Composer  
ENV COMPOSER_CACHE_DIR /cache/composer  
ENV COMPOSER_NO_INTERACTION 1  
# Composer: make global packages available for execution  
ENV PATH $PATH:/root/.composer/vendor/bin  
  
RUN apk update && apk upgrade \  
  
# build dependencies  
&& apk add \--no-cache --virtual .build-deps \  
curl \  
  
&& apk add \--no-cache \  
nodejs \  
fcgi \  
  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
  
# Composer speedup and tools  
&& composer global require hirak/prestissimo:@stable \  
"squizlabs/php_codesniffer=*" \  
"jakub-onderka/php-parallel-lint=*" \  
  
&& npm config set cache /cache/npm \  
&& npm install --global gulp \  
&& npm link gulp \  
  
# remove build dependencies  
&& apk del .build-deps  

