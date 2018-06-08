FROM alpine:3.4  
MAINTAINER Thoralf Liersch "thoralf.liersch@sysreport.de"  
RUN set -x \  
&& apk add --no-cache \  
git \  
bash \  
nginx \  
php5-fpm  
  
COPY configs/nginx.conf /etc/nginx/nginx.conf  
COPY configs/php-fpm.conf /etc/php5/php-fpm.conf  
COPY configs/default.conf /etc/nginx/conf.d/default.conf  
COPY configs/index.php /var/www/index.php  
  
COPY scripts/startup.sh /startup.sh  
CMD ["/startup.sh"]  

