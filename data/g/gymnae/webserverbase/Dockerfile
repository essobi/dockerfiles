#  
# nginx based mini webserver  
# with redis client and php-fpm  
#  
  
FROM gymnae/alpine-base:master  
MAINTAINER Gunnar Falk <docker@grundstil.de>  
  
# add packages  
RUN apk-install \  
php7-fpm@community \  
nginx \  
nginx-mod-http-redis2 \  
nginx-mod-http-upload-progress \  
nginx-mod-http-geoip \  
nginx-mod-http-cache-purge \  
nginx-mod-http-fancyindex \  
nginx-mod-rtmp \  
php7-openssl@community \  
#php7-cli@testing \  
php7-curl@community \  
php7-fpm@community \  
php7-gd@community \  
php7-redis@community \  
php7-pdo_mysql@community \  
php7-pgsql@community \  
libmaxminddb \  
php7-sqlite3@community  
# php7-zlib@community  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
&& mkdir -p /tmp/nginx \  
&& chown nginx /tmp/nginx  
  
# add an nginx user to avoid running as root and manage the mountpoint
properly  
RUN addgroup nginx www-data  
# && mkdir -p /var/www/localhost/htdocs \  
# && chown -R nginx:www-data /var/www/localhost/htdocs  
# copy the config  
COPY nginx.conf /etc/nginx/  
COPY php-fpm.conf /etc/php7/php-fpm.conf  
  
EXPOSE 80 443 8080 4443  
  
VOLUME ["/var/www/localhost/htdocs"]  
# run nginx  
CMD /usr/sbin/php-fpm7 ; /usr/sbin/nginx -g "daemon off;"  

