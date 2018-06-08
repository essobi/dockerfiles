ARG PHP_IMAGE_VERSION=7.2-alpine  
  
FROM php:${PHP_IMAGE_VERSION}  
  
LABEL maintainer fizzka <github.com/fizzka>  
  
ARG PHALCON_VERSION=3.3.1  
ARG PHALCON_EXT_PATH=php7/64bits  
  
RUN \  
curl -LO
https://github.com/phalcon/cphalcon/archive/v${PHALCON_VERSION}.tar.gz && \  
tar xzf v${PHALCON_VERSION}.tar.gz && \  
docker-php-ext-install -j $(getconf _NPROCESSORS_ONLN) \  
/cphalcon-${PHALCON_VERSION}/build/${PHALCON_EXT_PATH} && \  
rm -rf v${PHALCON_VERSION}.tar.gz /cphalcon-${PHALCON_VERSION}  

