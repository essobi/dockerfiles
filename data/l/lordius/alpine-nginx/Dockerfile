# lordius/alpine-nginx  
FROM alpine:latest  
LABEL maintainer=andriy.khomych@gmail.com  
# Install packages.  
RUN apk add --no-cache nginx ca-certificates openssl openssl-dev pcre-dev  
RUN adduser -D -u 1000 -g 'www' www  
RUN mkdir /etc/nginx/ssl/ && chown -R www:www /etc/nginx/ssl/  
RUN chown -R www:www /var/lib/nginx  
RUN chown -R www:www /var/www/localhost/htdocs  
RUN mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.orig  
ADD configs/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD configs/nginx/proxy_params /etc/nginx/proxy_params  
RUN openssl req -x509 -nodes -subj '/CN=localhost/O=My Company Name LTD./C=US'
-days 2048 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx-selfsigned.key -out
/etc/nginx/ssl/nginx-selfsigned.crt  
# Clean trash.  
RUN rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apk/* && \  
rm -rf /var/www/localhost/htdocs/*  
  
# Create /temp_configs_dir for using.  
RUN mkdir /temp_configs_dir && chmod -R +x /temp_configs_dir && cd
/temp_configs_dir  
# Fix permissions to nginx tmp  
RUN chmod -R +x /var/lib/nginx/tmp  
  
# Setup temp directory.  
WORKDIR /var/www/localhost/htdocs  
VOLUME ["/var/www/localhost/htdocs"]  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["docker-entrypoint.sh"]  
EXPOSE 80  

