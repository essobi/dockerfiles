FROM composer/composer  
MAINTAINER Mark Wienk <mark.wienk@trimm.nl>  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
zlib1g-dev \  
libicu-dev \  
g++  
RUN docker-php-ext-configure intl && \  
docker-php-ext-install intl  

