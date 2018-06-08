FROM alpine:3.3  
MAINTAINER "Daniel McCoy" <danielmccoy@gmail.com>  
  
RUN apk --update add wget curl git php php-curl php-openssl php-json php-phar
php-dom php-pdo php-ctype php-mysql php-xml php-zip php-gd  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
RUN mkdir -p /var/www  
  
WORKDIR /var/www  
  
VOLUME /var/www  
  
RUN composer self-update  
  
CMD ["bash"]  
  
ENTRYPOINT ["composer"]  
CMD ["--help"]  

