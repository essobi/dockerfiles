FROM ubuntu:14.04  
MAINTAINER Patrick Dos Santos <bdx.patrick.dossantos@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get -y dist-upgrade  
  
RUN apt-get -y install php5 php5-fpm php5-gd php5-ldap \  
php5-sqlite php5-pgsql php-pear php5-mysql \  
php5-mcrypt php5-xcache php5-xmlrpc  
  
RUN sed -i '/daemonize /c \  
daemonize = no' /etc/php5/fpm/php-fpm.conf  
  
RUN sed -i '/^listen /c \  
listen = 0.0.0.0:9000' /etc/php5/fpm/pool.d/www.conf  
  
RUN sed -i 's/^listen.allowed_clients/;listen.allowed_clients/'
/etc/php5/fpm/pool.d/www.conf  
  
EXPOSE 9000  
ENTRYPOINT ["php5-fpm"]

