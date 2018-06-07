# One of 'cli' or 'fpm' (as per https://hub.docker.com/_/php/).  
ARG PHP_TYPE  
ARG PHP_VERSION=7.2  
FROM lendingworks/php:${PHP_VERSION}-${PHP_TYPE}  
  
# Increment this to trigger a full rebuild.  
ENV CONTAINER_VERSION '1.0.0'  
ARG XDEBUG_VERSION=2.6.0  
RUN apk add --no-cache --update --virtual build-deps ${PHPIZE_DEPS} \  
&& pecl install xdebug-${XDEBUG_VERSION} \  
&& docker-php-ext-enable xdebug \  
&& rm -rf /tmp/pear \  
&& apk del --no-cache build-deps  
  
COPY ./conf/overrides.ini /usr/local/etc/php/conf.d/overrides.ini  
COPY ./conf/xdebug.ini /usr/local/etc/php/conf.d/xdebug.ini  
  
EXPOSE 9090 9000  

