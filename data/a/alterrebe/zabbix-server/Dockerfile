# Based on the work of "Mark Vartanyan <kolypto@gmail.com>":
https://github.com/kolypto/docker-zabbix-server  
# Using LTS ubuntu  
FROM ubuntu:trusty  
MAINTAINER Uri Savelchev <alterrebe@gmail.com>  
  
# Ignore APT warnings about not having a TTY  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8 locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN dpkg-reconfigure locales  
  
# Packages: update & install  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty multiverse" >
/etc/apt/sources.list.d/multiverse.list && \  
echo "deb http://archive.ubuntu.com/ubuntu/ trusty-updates multiverse" >>
/etc/apt/sources.list.d/multiverse.list && \  
apt-get update -qq  
RUN apt-get install -qq -y --no-install-recommends python-pip supervisor htop  
RUN apt-get install -qq -y --no-install-recommends nginx-full php5-fpm
php5-pgsql zabbix-server-pgsql zabbix-frontend-php snmp-mibs-downloader  
RUN pip install j2cli  
  
# Const  
ENV ZABBIX_PHP_TIMEZONE UTC  
  
# Add files  
ADD conf /root/conf  
  
# Configure: nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/default  
ADD conf/nginx-site.conf /etc/nginx/sites-enabled/zabbix  
RUN nginx -t  
  
# Configure: php  
RUN j2 /root/conf/php.ini > /etc/php5/mods-available/custom.ini  
RUN php5enmod custom  
# php-fpm socket has wrong permissions, so nginx can't access it :(  
RUN echo "listen.mode = 0666" >> /etc/php5/fpm/pool.d/www.conf  
  
# Configure: zabbix-server  
# broken package: pidfile dir is missing  
RUN mkdir -m0777 /var/run/zabbix/  
  
# Configure: supervisor  
ADD bin/dfg.sh /usr/local/bin/  
ADD conf/supervisor-all.conf /etc/supervisor/conf.d/  
  
# Runner  
ADD run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
  
# Declare  
VOLUME ["/etc/zabbix/alert.d/"]  
EXPOSE 80  
EXPOSE 10051  
CMD ["/root/run.sh"]  

