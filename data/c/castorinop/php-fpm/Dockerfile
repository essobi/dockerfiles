FROM alpine  
  
  
RUN apk add --update php5-zip php5-gd php5-cli php5-pdo_mysql php5-json
php5-posix php5-dom php5-xmlreader php5-xml php5-ctype php5-curl php5-zlib
php5-fpm php5-apcu  
  
#FROM php:fpm-alpine  
RUN set -ex \  
&& cd /etc/php5 \  
&& { \  
echo '[global]'; \  
echo 'error_log = /proc/self/fd/2'; \  
echo; \  
echo '[www]'; \  
echo '; if we send this to /proc/self/fd/1, it never appears'; \  
echo 'access.log = /proc/self/fd/2'; \  
echo; \  
echo 'clear_env = no'; \  
echo; \  
echo '; Ensure worker stdout and stderr are sent to the main error log.'; \  
echo 'catch_workers_output = yes'; \  
} | tee fpm.d/docker.conf \  
&& { \  
echo '[global]'; \  
echo 'daemonize = no'; \  
echo; \  
echo '[www]'; \  
echo 'listen = [::]:9000'; \  
} | tee fpm.d/zz-docker.conf \  
&& { \  
echo 'include = /etc/php5/fpm.d/*.conf'; \  
echo '[www]'; \  
echo 'user = nobody'; \  
echo 'group = nobody'; \  
echo 'pm = dynamic'; \  
echo 'pm.max_children = 5'; \  
echo 'pm.start_servers = 2'; \  
echo 'pm.min_spare_servers = 1'; \  
echo 'pm.max_spare_servers = 3'; \  
} | tee php-fpm.conf  
  
#FIX CONFIG remove 127.0.0.1:9000  
EXPOSE 9000  
CMD ["php-fpm"]  
  

