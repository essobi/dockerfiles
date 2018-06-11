FROM nginx:1  
  
COPY default.conf.tmpl /etc/nginx/conf.d/site.tmpl  
COPY run.sh /bin/run.sh  
ENV NGINX_LISTEN_PORT 80  
ENV NGINX_WEBROOT "/var/www/application/web"  
ENV NGINX_SERVERNAME nginx_pco  
ENV NGINX_INDEX_FILES index.php app.php app_dev.php index.php index.html  
ENV NGINX_TRY_FILES_XX /index.php\$is_args\$args /app.php\$is_args\$args
/app_dev.php\$is_args\$args  
ENV NGINX_TRY_FILES /index.php\$is_args\$args  
ENV NGINX_PHP_HOST_AND_PORT localhost:9000  
  
  
WORKDIR /var/www/application  
CMD /bin/run.sh  

