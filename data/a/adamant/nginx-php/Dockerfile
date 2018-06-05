# 3.4 does not have PHP-fpm for some reason....  
FROM alpine:3.3  
MAINTAINER Adam Dodman <adam.dodman@gmx.com>  
  
#Add all the Required packages for PHP, Nginx and Supervisord  
RUN apk add --no-cache nginx supervisor php-mcrypt php-soap php-openssl php-
pdo_odbc php-json php-dom php-pdo php-zip php-mysql php-sqlite3 php-apcu php-
pdo_pgsql php-bcmath \  
php-gd php-xcache php-odbc php-pdo_mysql php-pdo_sqlite php-gettext php-
xmlreader php-xmlrpc php-bz2 php-memcache php-mssql php-iconv php-pdo_dblib
php-curl php-ctype php-fpm  
  
#Setup the PHP config  
RUN sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= 0|i" /etc/php/php.ini &&
\  
sed -i "s|;*daemonize\s*=\s*yes|daemonize = no|g" /etc/php/php-fpm.conf  
  
# Forward request and error logs to docker log collector:
http://serverfault.com/a/634296  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Add all the configs to the correct place  
COPY configs/nginx.conf /etc/nginx/nginx.conf  
COPY configs/common.conf /etc/nginx/common.conf  
COPY configs/default.conf /etc/nginx/default.conf  
COPY configs/supervisord.conf /etc/supervisord.conf  
  
# Set Docker defaults  
WORKDIR /var/www  
VOLUME ["/etc/nginx/conf.d", "/var/www"]  
EXPOSE 80 443  
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

