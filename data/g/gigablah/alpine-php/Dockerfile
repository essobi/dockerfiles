FROM gigablah/alpine-base:3.2  
RUN apk add -U php php-fpm php-json php-ctype php-curl php-openssl nginx ca-
certificates \  
&& rm -rf /var/cache/apk/*  
  
ADD config/nginx.conf /etc/nginx/nginx.conf  
ADD config/sites/*.conf /etc/nginx/sites-enabled/  
ADD service/nginx/run /etc/service/nginx/run  
ADD config/php-fpm.conf /etc/php/php-fpm.conf  
ADD service/php-fpm/run /etc/service/php-fpm/run  
  
RUN chmod +x /etc/service/nginx/run \  
&& chmod +x /etc/service/php-fpm/run  
  
VOLUME ["/opt/www"]  
  
EXPOSE 80 443  

