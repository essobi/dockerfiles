  
FROM centos:7  
MAINTAINER Wenbin Hou <catchyrime@fastmail.com>  
  
SHELL [ "/bin/bash", "-c" ]  
  
COPY rt/opt/nginx /opt/nginx  
COPY rt/etc/nginx /etc/nginx  
COPY rt/var/log/nginx /var/log/nginx  
COPY rt/tmp/nginx /tmp/nginx  
  
RUN \  
set -xe; \  
YUM_OPTION='--quiet --noplugins --assumeyes'; \  
yum $YUM_OPTION install gd geoip; \  
yum $YUM_OPTION clean all; \  
\  
mkdir /var/www; \  
groupadd --gid 33 www-data; \  
useradd --uid 33 --gid www-data --home-dir /var/www --shell /sbin/nologin
--no-create-home --no-user-group www-data; \  
chown -R www-data:www-data /tmp/nginx; \  
chown -R www-data:www-data /var/log/nginx; \  
\  
ln -sfT /opt/nginx/sbin/nginx /usr/local/bin/nginx  
  
ENTRYPOINT [ "nginx" ]  
CMD [ "-g", "daemon off;" ]  
  
VOLUME /var/log/nginx  
VOLUME /etc/nginx  
VOLUME /var/www  
  
EXPOSE 80/tcp  
EXPOSE 443/tcp  
  

