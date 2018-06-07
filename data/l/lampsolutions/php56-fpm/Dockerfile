FROM ubuntu:14.04  
MAINTAINER Pavel Litvyak <pvlltvk@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV POSTFIX_IP 127.0.0.1  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list && \  
apt-get update && \  
apt-get -y dist-upgrade  
  
RUN echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu trusty main" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-key E5267A6C && \  
apt-get update  
  
RUN apt-get -y install php5.6 php5.6-gd php5.6-ldap \  
php5.6-sqlite php5.6-pgsql php-pear php5.6-mysql \  
php5.6-mcrypt php5.6-xmlrpc php5.6-fpm php5.6-curl php5.6-xml php5.6-mbstring
nullmailer supervisor hostname curl \  
php5.6-gd php5.6-sqlite3  
  
RUN update-alternatives --set php /usr/bin/php5.6  
  
RUN sed -i '/daemonize /c \  
daemonize = no' /etc/php/5.6/fpm/php-fpm.conf  
  
RUN sed -i '/error_log /c \  
error_log = /var/log2/php5.6-fpm.log' /etc/php/5.6/fpm/php-fpm.conf  
  
RUN sed -i '/^listen /c \  
listen = 0.0.0.0:9000' /etc/php/5.6/fpm/pool.d/www.conf  
  
RUN sed -i '/^pm.max_children /c \  
pm.max_children = 50' /etc/php/5.6/fpm/pool.d/www.conf  
  
RUN sed -i '/^pm.start_servers /c \  
pm.start_servers = 5' /etc/php/5.6/fpm/pool.d/www.conf  
  
RUN sed -i '/^pm.max_spare_servers /c \  
pm.max_spare_servers = 5' /etc/php/5.6/fpm/pool.d/www.conf  
  
RUN sed -i 's/^listen.allowed_clients/;listen.allowed_clients/'
/etc/php/5.6/fpm/pool.d/www.conf  
  
RUN mkdir -p /var/log/php5-fpm && \  
chown -R www-data:www-data /var/log/php5-fpm \  
&& mkdir -p /run/php/  
  
RUN mkdir /etc/php/conf.d  
  
RUN mkdir /etc/php/ini/  
RUN touch /etc/php/ini/php.ini  
RUN ln -s /etc/php/ini/php.ini /etc/php/5.6/cli/conf.d/30-php.ini  
RUN ln -s /etc/php/ini/php.ini /etc/php/5.6/fpm/conf.d/30-php.ini  
RUN rm /etc/php/ini/php.ini  
  
RUN mkdir /opt/extras  
  
RUN echo "include=/etc/php/conf.d/*.conf" >> /etc/php/5.6/fpm/pool.d/www.conf  
  
RUN rm -f /var/spool/nullmailer/trigger \  
&& mkfifo /var/spool/nullmailer/trigger \  
&& chown mail:root /var/spool/nullmailer/trigger \  
&& chmod 0622 /var/spool/nullmailer/trigger  
  
COPY ./config/supervisor/conf.d /etc/supervisor/conf.d  
  
EXPOSE 9000  
CMD echo $POSTFIX_IP smtp > /etc/nullmailer/remotes && \  
echo $MAILNAME > /etc/mailname && \  
echo $HOSTNAME > /etc/hostname && \  
mkdir -p $FPM_DIR && \  
chown -R www-data:www-data $FPM_DIR && \  
/usr/bin/supervisord -n -c "/etc/supervisor/supervisord.conf"  
  

