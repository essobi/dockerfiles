FROM alpine  
RUN apk add --no-cache bash nginx ca-certificates php-fpm php-json php-zlib
php-xml php-pdo php-phar php-openssl php-pdo_mysql php-mysqli php-gd php-iconv
php-mcrypt  
ADD files/run.sh /run.sh  
RUN chmod +x /run.sh  
RUN chown -R nginx:www-data /var/lib/nginx  
ADD files/nginx.conf /etc/nginx/nginx.conf  
ADD files/00-default.conf /etc/nginx/conf.d/00-default.conf  
ADD files/php /etc/nginx/php  
ADD files/php-fpm.conf /etc/php/php-fpm.conf  
  
EXPOSE 80  
VOLUME "/usr/share/nginx/"  
WORKDIR "/usr/share/nginx/"  
  
CMD ["/run.sh"]  

