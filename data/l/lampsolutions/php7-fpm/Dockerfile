FROM ubuntu:16.04  
MAINTAINER Pavel Litvyak <pvlltvk@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial-backports main" >
/etc/apt/sources.list  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main" >>
/etc/apt/sources.list  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial multiverse" >>
/etc/apt/sources.list  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial universe" >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get -y dist-upgrade  
  
RUN apt-get -y install php7.0 php7.0-gd php7.0-ldap \  
php7.0-sqlite php7.0-pgsql php-pear php7.0-mysql \  
php7.0-mcrypt php7.0-xmlrpc php7.0-fpm php7.0-curl php7.0-xml php7.0-zip
php7.0-soap nullmailer supervisor vim hostname curl php7.0-gd php7.0-mbstring
php7.0-sqlite3 php-geoip  
  
RUN mkdir -p "/run/php/"  
  
RUN sed -i '/daemonize /c \  
daemonize = no' /etc/php/7.0/fpm/php-fpm.conf  
  
RUN sed -i '/error_log /c \  
error_log = /var/log2/php7.0-fpm.log' /etc/php/7.0/fpm/php-fpm.conf  
  
RUN sed -i '/^listen /c \  
listen = 0.0.0.0:9000' /etc/php/7.0/fpm/pool.d/www.conf  
  
RUN sed -i '/^pm.max_children /c \  
pm.max_children = 50' /etc/php/7.0/fpm/pool.d/www.conf  
  
RUN sed -i '/^pm.start_servers /c \  
pm.start_servers = 5' /etc/php/7.0/fpm/pool.d/www.conf  
  
RUN sed -i '/^pm.max_spare_servers /c \  
pm.max_spare_servers = 5' /etc/php/7.0/fpm/pool.d/www.conf  
  
RUN sed -i 's/^listen.allowed_clients/;listen.allowed_clients/'
/etc/php/7.0/fpm/pool.d/www.conf  
  
RUN mkdir -p /var/log/php7-fpm && \  
chown -R www-data:www-data /var/log/php7-fpm  
  
RUN mkdir /etc/php/conf.d  
RUN mkdir /opt/extras  
RUN mkdir /etc/php/ini/  
  
RUN echo "include=/etc/php/conf.d/*.conf" >> /etc/php/7.0/fpm/pool.d/www.conf  
  
RUN rm -f /var/spool/nullmailer/trigger \  
&& mkfifo /var/spool/nullmailer/trigger \  
&& chown mail:root /var/spool/nullmailer/trigger \  
&& chmod 0622 /var/spool/nullmailer/trigger  
  
COPY ./config/supervisor/conf.d /etc/supervisor/conf.d  
  
EXPOSE 9000  
CMD echo $POSTFIX_IP smtp > /etc/nullmailer/remotes && \  
echo $MAILNAME > /etc/mailname && \  
echo $HOSTNAME > /etc/hostname && \  
echo "172.17.0.1 $MYSQLNAME" >> /etc/hosts && \  
mkdir -p $FPM_DIR && \  
chown -R www-data:www-data $FPM_DIR && \  
/usr/bin/supervisord -n -c "/etc/supervisor/supervisord.conf"  

