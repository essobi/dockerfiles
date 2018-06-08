FROM ej52/alpine-nginx-php:latest  
LABEL autor = "Daniel Mora Pastor"  
  
ENV MYSQL_ROOT_PASSWORD secret  
  
RUN apk update && \  
apk add mariadb mariadb-client  
  
RUN rm /etc/nginx/conf.d/default.conf  
COPY default.conf /etc/nginx/conf.d/default.conf  
  
RUN mkdir /mariadb-initdb.d  
  
# comment out a few problematic configuration values  
# don't reverse lookup hostnames, they are usually another container  
RUN sed -Ei 's/^(bind-address|log)/#&/' /etc/mysql/my.cnf \  
&& echo -e 'skip-host-cache\nskip-name-resolve' | awk '{ print } $1 ==
"[mysqld]" && c == 0 { c = 1; system("cat") }' /etc/mysql/my.cnf > /tmp/my.cnf
\  
&& mv /tmp/my.cnf /etc/mysql/my.cnf  
  
RUN rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
COPY mariadb-setup.sh /  
  
RUN sh mariadb-setup.sh  
  
WORKDIR /var/www  
  
RUN composer create-project --prefer-dist laravel/laravel laravel  
  
WORKDIR /var/www/laravel  
  
RUN rm .env && \  
rm app/Providers/AppServiceProvider.php  
  
COPY .env /var/www/laravel/.env  
COPY AppServiceProvider.php app/Providers/AppServiceProvider.php  
  
RUN echo "DB_PASSWORD=${MYSQL_ROOT_PASSWORD}" >> /var/www/laravel/.env  
  
RUN php artisan make:auth  

