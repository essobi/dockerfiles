FROM alpine:latest  
  
MAINTAINER LM <treerootboy@gmail.com>  
  
RUN apk add --update php php-fpm php-mcrypt php-gd php-memcache php-mysql php-
openssl php-opcache php-xml php-soap php-pdo \  
&& rm -rf /var/cache/apk/* \  
&& adduser -u8080 -D -H www  
  
COPY php-fpm.conf /etc/php-fpm.conf  
  
EXPOSE 9000  
WORKDIR /www  
VOLUME /www  
  
CMD php-fpm -F -y /etc/php-fpm.conf  

