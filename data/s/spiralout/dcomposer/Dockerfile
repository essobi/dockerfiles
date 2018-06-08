FROM alpine:3.1  
MAINTAINER "SpiralOut" <spiralout.eu@gmail.com>  
  
RUN apk --update add wget curl git php php-curl php-openssl php-json php-phar
php-dom php-pdo  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
RUN mkdir -p /var/www  
  
WORKDIR /var/www  
  
VOLUME /var/www  
  
RUN composer self-update  
  
CMD ["bash"]  
  
ENTRYPOINT ["composer"]  
CMD ["--help"]  

