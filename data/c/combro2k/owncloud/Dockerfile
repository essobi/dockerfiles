# Includes php-fpm, cron job support and PostgreSQL support  
FROM ubuntu-debootstrap:14.04  
MAINTAINER Martijn van Maurik <docker@vmaurik.nl>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62  
RUN echo deb http://nginx.org/packages/mainline/ubuntu trusty nginx >
/etc/apt/sources.list.d/nginx-stable-trusty.list  
  
RUN mkdir -p /var/www  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends curl nginx supervisor php5-fpm
php5-pgsql php5-mysql php5-intl php5-gd php-xml-parser php5-curl cron
smbclient \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& cd /var/www \  
&& curl -sSL -k https://download.owncloud.org/community/owncloud-7.0.2.tar.bz2
| tar jx \  
&& chown -R www-data:www-data /var/www/owncloud  
  
ADD config/etc/crontab /etc/crontab  
ADD config/etc/nginx/nginx.conf /etc/nginx/nginx.conf  
ADD config/etc/nginx/server.conf /etc/nginx/server.conf  
ADD config/etc/php5 /etc/php5  
ADD config/etc/supervisor/supervisord.conf /etc/supervisor/supervisord.conf  
ADD config/etc/supervisor/conf.d /etc/supervisor/conf.d  
ADD config/init /init  
  
RUN mkdir -p /etc/nginx/scripts  
ADD config/etc/nginx/proxy_client_ip.php
/etc/nginx/scripts/proxy_client_ip.php  
  
VOLUME ["/var/www/owncloud/data", "/var/www/owncloud/config"]  
EXPOSE 5000  
CMD ["/init"]  

