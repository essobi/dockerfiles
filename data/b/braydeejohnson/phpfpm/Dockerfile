FROM braydeejohnson/php:7.0  
  
MAINTAINER "Braydee Johnson" <braydee@braydeejohnson.com>  
  
RUN apt-get update -y && \  
apt-get install -y \  
php7.0-fpm  
  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/"
/etc/php/7.0/fpm/php.ini && \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php/7.0/fpm/php.ini &&
\  
sed -i "s/display_errors = Off/display_errors = stderr/"
/etc/php/7.0/fpm/php.ini && \  
sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 30M/"
/etc/php/7.0/fpm/php.ini && \  
sed -i "s/;opcache.enable=0/opcache.enable=0/" /etc/php/7.0/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-
fpm.conf && \  
sed -i "/listen = .*/c\listen = [::]:9000" /etc/php/7.0/fpm/pool.d/www.conf &&
\  
sed -i "/pid = .*/c\;pid = /run/php/php7.0-fpm.pid" /etc/php/7.0/fpm/php-
fpm.conf && \  
sed -i '/^listen.allowed_clients/c;listen.allowed_clients ='
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i '/^;catch_workers_output/ccatch_workers_output = yes'
/etc/php/7.0/fpm/pool.d/www.conf && \  
sed -i '/^;env\\[TEMP\\] = .*/aenv[DB_PORT_3306_TCP_ADDR] =
$DB_PORT_3306_TCP_ADDR' /etc/php/7.0/fpm/pool.d/www.conf  
  
RUN echo "xdebug.max_nesting_level = 1024" >> /etc/php/7.0/mods-
available/xdebug.ini  
  
RUN echo "extension=mongodb.so" > /etc/php/7.0/fpm/conf.d/20-mongodb.ini && \  
echo "extension=mongodb.so" > /etc/php/7.0/cli/conf.d/20-mongodb.ini && \  
echo "extension=mongodb.so" > /etc/php/7.0/mods-available/mongodb.ini  
  
RUN mkdir -p /data  
VOLUME ["/data"]  
  
EXPOSE 9000  
  
ENTRYPOINT ["/usr/sbin/php-fpm7.0", "-F"]

