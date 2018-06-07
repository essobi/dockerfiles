FROM php:7.1.9-alpine  
MAINTAINER hitalos <hitalos@gmail.com>  
  
RUN apk update && apk upgrade && apk add git  
  
# Install PHP extensions  
ADD install-php.sh /usr/sbin/install-php.sh  
RUN /usr/sbin/install-php.sh  
  
# Download and install NodeJS  
ENV NODE_VERSION 8.6.0  
ENV YARN_VERSION 1.1.0  
ENV NPM_CONFIG_LOGLEVEL info  
  
ADD install-node.sh /usr/sbin/install-node.sh  
RUN /usr/sbin/install-node.sh  
# RUN npm i -g yarn  
WORKDIR /var/www  
RUN npm install  
# CMD php ./artisan serve --port=80 --host=0.0.0.0  
# EXPOSE 80  
HEALTHCHECK \--interval=1m CMD curl -f http://localhost/ || exit 1  

