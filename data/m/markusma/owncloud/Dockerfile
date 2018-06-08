# OwnCloud 7.0, nginx, etcd registration, confd and supervisord on Ubuntu
Trusty  
#  
# Includes php-fpm, cron job support and PostgreSQL support  
FROM markusma/nginx-etcdregister:1.7  
MAINTAINER Markus Mattinen <markus@gamma.fi>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends php5-fpm php5-pgsql php5-mysql
php5-intl php5-gd php-xml-parser php5-curl cron \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& cd /var/www \  
&& curl -sSL http://download.owncloud.org/community/owncloud-7.0.4.tar.bz2 |
tar jx \  
&& chown -R www-data:www-data /var/www/owncloud  
  
ADD config/etc/crontab /etc/crontab  
ADD config/etc/nginx/server.conf /etc/nginx/server.conf  
ADD config/etc/php5 /etc/php5  
ADD config/etc/supervisor/conf.d /etc/supervisor/conf.d  
ADD config/init /init  
  
VOLUME ["/var/www/owncloud/data", "/var/www/owncloud/config"]  
EXPOSE 5000  

