FROM cubeteam/alpine-php  
  
LABEL description="A Docker image based on Alpine Linux for running nginx and
PHP-FPM with MongoDB extension"  
LABEL maintainer="n.vasic@cubeteam.com"  
  
RUN apk --update add \  
alpine-sdk \  
openssl-dev \  
php7-pear \  
php7-dev \  
&& rm -rf /var/cache/apk/*  
  
RUN pecl install mongodb \  
&& pecl clear-cache  
  
RUN echo "extension=mongodb.so" > /etc/php7/conf.d/mongodb.ini  

