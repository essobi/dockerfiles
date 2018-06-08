FROM alpine:3.4  
RUN \  
adduser -S -D www-data && \  
addgroup www-data && \  
adduser www-data www-data && \  
echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing/" >>
/etc/apk/repositories && \  
apk add --no-cache php5-fpm nginx gettext libcgroup-tools@testing && \  
rm /etc/php5/php.ini  
  
COPY php-fpm.conf /etc/php5/  
COPY default.ini /etc/php5/conf.d/  
COPY nginx.conf.template /etc/nginx/  
COPY php-fpm-wrapper nginx-wrapper /usr/local/sbin/  
  
EXPOSE 80 9000  
CMD ["php-fpm-wrapper"]  

