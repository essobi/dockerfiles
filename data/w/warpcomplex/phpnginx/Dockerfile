##########################################################################  
## ##  
## Docker file of Docker image with NGINX and PHP for WARP projects ##  
## ##  
##########################################################################  
## Table of contents  
##  
## 1. Base image and developers  
## 2. Suppress messages error/warning from upstart  
## 3. Let the container know about the absence of tty  
## 4. Erase of script file /usr/sbin/policy-rc.d  
## 5. Update packages info, install additional  
## 6. Install necessary packages  
## 7. Create that cats, if they absent  
## 8. Delete nginx and php configs  
## 9. Expose some ports  
## 10. Add bootstrap.sh script to image  
## 11. Set default cmd  
## 12. Install composer  
## 13. Prepare logs for postfix  
##  
# 1. Base image and developers  
FROM ubuntu:16.04  
MAINTAINER German Manvelov <gtmmm2011@gmail.com>  
  
# 2. Suppress messages error/warning from upstart  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# 3. Let the container know about the absence of tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# 4. Erase of script file /usr/sbin/policy-rc.d  
# - Это позволит избежать появления ошибки: invoke-rc.d: policy-rc.d denied
execution of start  
# - Подробнее см.здесь: https://habrahabr.ru/post/247903/  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
# 5. Update packages info, install additional  
RUN apt-get update && apt-get -y upgrade  
  
# 6. Install necessary packages  
# 6.1. Uncomment this if you need postfix log  
# - Log location: other/logs/mail.log  
RUN apt-get update && apt-get install -y syslog-ng syslog-ng-core; exit 0  
  
# 6.2. Install necessary packages  
RUN apt-get update && apt-get install -y \  
  
curl \  
cron \  
supervisor \  
nginx \  
php7.0 php7.0-fpm php7.0-gmp php7.0-mbstring php7.0-zip \  
git \  
php7.0-mysql \  
php7.0-curl \  
php7.0-gd \  
php7.0-intl \  
php7.0-mcrypt \  
php7.0-sqlite \  
php7.0-tidy \  
php7.0-xmlrpc \  
php7.0-xsl \  
php7.0-pgsql \  
php7.0-ldap \  
pwgen \  
sshpass \  
git-all \  
mailutils \  
nano \  
php7.0-bcmath \  
; exit 0  
# 6.3. Install TOR  
# 1] Install  
RUN echo "deb http://deb.torproject.org/torproject.org xenial main" >>
/etc/apt/sources.list  
RUN echo "deb-src http://deb.torproject.org/torproject.org xenial main" >>
/etc/apt/sources.list  
RUN gpg --keyserver keys.gnupg.net --recv
A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89  
RUN gpg --export A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89 | apt-key add -  
RUN apt-get update && apt-get install -y tor deb.torproject.org-keyring; exit
0  
  
# 2] Turn on TOR autostart (to control that via supervisord)  
RUN systemctl disable tor.service  
  
# 7. Create that cats, if they absent  
RUN mkdir -p /etc/nginx  
RUN mkdir -p /var/log/supervisor  
RUN mkdir -p /var/run/php-fpm  
  
# 8. Delete nginx and php configs  
# - (to add that configs vie docker compose config)  
RUN rm /etc/nginx/nginx.conf  
RUN rm /etc/php/7.0/fpm/php.ini  
  
# 9. Expose some ports  
EXPOSE 80  
EXPOSE 443  
EXPOSE 25  
EXPOSE 587  
EXPOSE 465  
EXPOSE 993  
EXPOSE 143  
EXPOSE 110  
EXPOSE 995  
# 10. Add bootstrap.sh script to image  
# ADD bootstrap.sh /opt/bootstrap.sh  
# RUN chmod +x /opt/bootstrap.sh  
# 11. Set default cmd  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.d/supervisor-docker-
nginx_phpfpm-dev.ini"]  
  
# 12. Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
# 13. Prepare logs for postfix  
# 13.1. Replace the system() source because inside Docker we can't access
/proc/kmsg.  
# https://groups.google.com/forum/#!topic/docker-user/446yoB0Vx6w  
RUN sed -i -E 's/^(\s*)system\\(\\);/\1unix-stream("\/dev\/log");/'
/etc/syslog-ng/syslog-ng.conf  
  
# 13.2. Uncomment 'SYSLOGNG_OPTS="--no-caps"' to avoid the following warning:  
# syslog-ng: Error setting capabilities, capability management disabled;
error='Operation not permitted'  
# http://serverfault.com/questions/524518/error-setting-capabilities-
capability-management-disabled#  
RUN sed -i 's/^#\\(SYSLOGNG_OPTS="--no-caps"\\)/\1/g' /etc/default/syslog-ng  
  

