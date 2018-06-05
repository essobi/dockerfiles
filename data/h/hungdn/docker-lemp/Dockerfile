# nginx/php  
# VERSION 0.1  
FROM ubuntu:14.04  
MAINTAINER Hung Dinh <hung.dnc@gmail.com>  
  
# Update base image  
# Add sources for latest nginx  
# Install software requirements  
RUN # Get some security updates  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# install nginx, php5, mysql driver and supervisor  
RUN apt-get -y install supervisor nginx php5-fpm git php5-mysql php-apc
php5-curl php5-gd php5-intl php5-mcrypt php5-memcache php5-sqlite php5-tidy
php5-xmlrpc php5-xsl php5-pgsql php5-mongo php5-ldap pwgen  
  
RUN apt-get autoremove -y  
RUN apt-get clean  
RUN apt-get autoclean  
RUN echo -n > /var/lib/apt/extended_states  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /usr/share/man/??  
RUN rm -rf /usr/share/man/??_*  
  
# Add our config files  
ADD conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
ADD conf/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ADD conf/php.ini /etc/php5/fpm/php.ini  
  
# disable the daemons for nginx & php  
# RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
# RUN sed -i "s/;daemonize = yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf  
# sites volume  
RUN mkdir /home/www  
RUN echo "<?php phpinfo() ?>" > /home/www/index.php  
  
# Define mountable directories.  
VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/sites-available",
"/var/log/nginx", "/home/www"]  
# Path to your conf file & sites-* .  
# Mount with `-v <data-dir>:/etc/nginx/sites-enabled`  
# expose http & https  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/bin/supervisord"]  

