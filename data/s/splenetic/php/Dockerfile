FROM alpine:3.2  
RUN apk update && apk upgrade  
RUN apk add php-fpm php-mcrypt php-curl php-ctype php-json php-openssl  
RUN apk add nginx supervisor  
  
RUN mkdir /tmp/nginx  
RUN addgroup -g 1000 -S www  
RUN adduser -h /var/www -S -s /bin/false -D -u 1000 -G www www  
  
EXPOSE 80  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD supervisord.conf /etc/supervisord.conf  
VOLUME /var/www  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

