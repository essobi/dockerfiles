FROM nginx:alpine  
LABEL maintainer="Benedikt Franke <benedikt.franke@zoho.com>"  
  
RUN mkdir /var/www  
  
ENV WEB_ROOT=/var/www/public  
ENV PHP_SERVER=php  
ENV PHP_PORT=9000  
# ensure www-data user exists  
RUN set -x \  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data  
  
COPY content /  
  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

