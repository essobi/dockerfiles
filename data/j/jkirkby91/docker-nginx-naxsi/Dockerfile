FROM jkirkby91/ubuntusrvbase:latest  
  
MAINTAINER James Kirkby <info@watchoutforsnakes.co.uk>  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install nginx -y --fix-missing && \  
apt-get remove --purge -y software-properties-common build-essential && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
echo -n > /var/lib/apt/extended_states && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
RUN mkdir -p /srv/ssl && \  
mkdir -p /srv/log && \  
mkdir -p /srv/log/nginx && \  
mkdir -p /srv/confs && \  
mkdir -p /srv/confs/nginx  
  
COPY confs/nginx/naxsi_core.rules /etc/nginx/naxsi_core.rules  
  
COPY confs/nginx/naxsi.rules /etc/nginx/naxsi.rules  
  
RUN cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local && \  
touch /etc/fail2ban/filter.d/nginx-req-limit.conf  
  
COPY confs/fail2ban/nginx-req-limit.conf /etc/fail2ban/filter.d/nginx-req-
limit.conf  
  
COPY confs/apparmor/nginx.conf /etc/apparmor.d/nginx.conf  
  
COPY confs/fail2ban/jail1.conf /tmp/jail.conf  
  
RUN cat /tmp/jail.conf >> /etc/fail2ban/jail.local && \  
rm /tmp/jail.conf  
  
COPY confs/fail2ban/nginx-naxsi.conf /etc/fail2ban/filter.d/nginx-naxsi.conf  
  
COPY confs/fail2ban/jail2.conf /tmp/jail.conf  
  
RUN cat /tmp/jail.conf >> /etc/fail2ban/jail.conf  
  
COPY confs/supervisord/supervisord.conf /etc/supervisord.conf  
  
COPY confs/nginx/nginx.conf /etc/nginx/nginx.conf  
  
COPY start.sh /start.sh  
  
RUN touch /run/nginx.pid && \  
usermod -u 1000 www-data && \  
chown -Rf www-data:www-data /run/nginx.pid && \  
mkdir /var/lib/nginx/body && \  
mkdir /var/lib/nginx/proxy && \  
mkdir /var/lib/nginx/fastcgi && \  
mkdir /var/lib/nginx/uwsgi && \  
mkdir /var/lib/nginx/scgi && \  
chown -Rf www-data:www-data /var/lib/nginx && \  
chmod 777 /start.sh && \  
touch /srv/log/nginx.access.log && \  
touch /srv/log/nginx.error.log && \  
chown -Rf www-data:www-data /srv && \  
chmod 755 /srv && \  
find /srv -type d -exec chmod 755 {} \; && \  
find /srv -type f -exec chmod 644 {} \; && \  
chown -Rf www-data:www-data /var/log/nginx  
  
EXPOSE 1025  
  
WORKDIR /srv  
  
VOLUME ["/srv"]  
  
USER www-data  
  
CMD ["/bin/bash", "/start.sh"]  

