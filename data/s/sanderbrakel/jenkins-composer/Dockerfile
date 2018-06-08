# Composer Docker Container  
# sanderbrakel/jenkins-composer:1.1  
FROM composer/composer:1.1  
MAINTAINER Ultraware  
  
# install GD  
RUN apt-get update && apt-get install -y \  
libgmp-dev \  
&& ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/include/gmp.h \  
&& docker-php-ext-install gmp \

