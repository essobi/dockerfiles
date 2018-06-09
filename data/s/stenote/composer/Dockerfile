FROM alpine:3.2  
RUN apk update && \  
apk add php-cli php-phar php-openssl php-json php-dom php-pdo curl git && \  
rm -rf /var/cache/*  
  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
WORKDIR /usr/src/app  
  
ENTRYPOINT ["composer", "--prefer-source"]  

