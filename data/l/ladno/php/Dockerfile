FROM webdevops/php:alpine  
RUN apk-install php7-imagick  
RUN apk-install openssl-dev autoconf g++ make  
RUN pecl install mongodb && \  
echo "extension=mongodb.so" > /etc/php7/conf.d/ext-mongo.ini  

