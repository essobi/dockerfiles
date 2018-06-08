FROM jkirkby91/docker-php7-fpm:latest  
MAINTAINER James Kirkby <jkirkby@protonmail.ch>  
  
USER root  
  
COPY confs/apt/preferences.d/pdns /etc/apt/preferences.d/pdns  
RUN apt-get update && apt-get upgrade -y \  
&& curl https://repo.powerdns.com/FD380FBB-pub.asc | apt-key add - \  
&& echo "deb [arch=amd64] http://repo.powerdns.com/ubuntu xenial-auth-40 main"
> /etc/apt/sources.list.d/pdns.list  
  
RUN apt-get update && apt-get install -y \  
mysql-client \  
pdns-server \  
pdns-backend-mysql \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY confs/apparmor_pdns /etc/apparmor.d/apparmor_pdns  
  
RUN rm -Rf /etc/powerdns/*  
COPY confs/pdns/pdns.conf /etc/powerdns/pdns.conf  
COPY confs/pdns/pdns.d/ /etc/powerdns/pdns.d/  
COPY confs/poweradmin/config.inc.php /srv/  
  
RUN chmod 644 /etc/powerdns/pdns.d/pdns.*  
  
RUN usermod -u 1000 www-data && \  
chown -Rf www-data:www-data /srv && \  
chown -Rf www-data:www-data /etc/powerdns && \  
chmod 755 /srv  
  
RUN find /srv -type d -exec chmod 755 {} \; && \  
find /srv -type f -exec chmod 644 {} \;  
  
### SUPERVISOR ###  
COPY confs/supervisord/supervisord.conf /etc/supervisord.conf  
  
COPY start.sh /start.sh  
RUN chmod 777 /start.sh  
  
EXPOSE 1025  
EXPOSE 1025/udp  
  
RUN usermod -a -G pdns www-data  
  
USER www-data  
  
CMD ["/bin/bash", "/start.sh"]  

