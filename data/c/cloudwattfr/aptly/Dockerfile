FROM debian:jessie  
  
RUN echo "deb http://repo.aptly.info/ squeeze main" >
/etc/apt/sources.list.d/aptly.list; \  
apt-key adv --keyserver keys.gnupg.net --recv-keys 2A194991; \  
apt-get update; \  
apt-get install aptly wget nginx xz-utils bzip2 -y --force-yes; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget -O /usr/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-
amd64 && chmod +x /usr/bin/confd  
  
ADD entrypoint.sh /entrypoint.sh  
ADD conf/* /etc/confd/conf.d/  
ADD templates/* /etc/confd/templates/  
ADD files/deb-mirror.sh /etc/cron.daily/deb-mirror  
ADD nginx.conf /etc/nginx/sites-available/default  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["nginx", "-g", "'daemon off;'"]  

