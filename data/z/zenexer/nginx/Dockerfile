# Nginx and PHP-FPM  
#  
# Volumes are /conf, /sites, and /var/log. Put your per-instance configuration  
# files in /conf; for shared configuration files, use /etc/nginx and
/etc/php5.  
# Unfortunately, there's no include directive in php.ini, so there's no  
# /conf/php5-fpm directory. You can put your website files in /sites (not  
# configuration files).  
#  
# VERSION 1.0.0  
FROM stackbrew/ubuntu:saucy  
MAINTAINER Paul Buonopane <paul+docker@earth2me.com>  
  
VOLUME [ "/conf", "/var/log", "/sites" ]  
  
# Ensure that we are up-to-date  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
  
RUN apt-get install -y nginx php5-fpm  
  
# Use volumes  
RUN rm -Rf /etc/nginx/sites-enabled/default /var/log/nginx /var/log/php5-fpm  
RUN echo 'include /conf/nginx/*;' > /etc/nginx/conf.d/docker.conf  
  
# Common extensions  
RUN apt-get install -y php-pear php5-json php5-mysqlnd php5-gd php5-curl
php5-imagick php5-memcache php5-memcached  
  
# Run in foreground  
CMD [ -d /conf/nginx ] || mkdir /conf/nginx; [ -d /var/log/nginx ] || mkdir
/var/log/nginx; php5-fpm -FR & nginx -g "daemon off;" & wait  

