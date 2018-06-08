FROM alpine:3.4  
RUN apk --update add nginx php5-fpm && \  
mkdir -p /var/log/nginx && \  
touch /var/log/nginx/access.log && \  
mkdir -p /tmp/nginx && \  
mkdir -p /run/nginx && \  
echo "clear_env = no" >> /etc/php5/php-fpm.conf  
ADD www /www  
ADD nginx.conf /etc/nginx/  
EXPOSE 80  
CMD php-fpm -d variables_order="EGPCS" && (tail -F /var/log/nginx/access.log
&) && exec nginx -g "daemon off;"  

