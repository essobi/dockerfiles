FROM chambana/uwsgi-php:latest  
  
MAINTAINER Josh King <jking@chambana.net>  
  
RUN apt-get -qq update && \  
apt-get install -y --no-install-recommends roundcube-core \  
roundcube-pgsql \  
roundcube-plugins \  
roundcube-plugins-extra && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV ROUNDCUBE_DBUSER=roundcube \  
ROUNDCUBE_DBNAME=roundcube \  
ROUNDCUBE_DBSERVER=postgres  
  
ADD files/uwsgi/roundcube.conf /etc/uwsgi/apps-available/roundcube.conf  
ADD files/dbconfig/roundcube.conf /etc/dbconfig-common/roundcube.conf  
  
EXPOSE 80  
## Add startup script.  
ADD bin/run.sh /app/bin/run.sh  
RUN chmod 0755 /app/bin/run.sh  
  
CMD ["/app/bin/run.sh"]  
CMD ["uwsgi", "--uid", "www-data", "--gid", "www-data", "--ini",
"/etc/uwsgi/apps-available/roundcube.conf"]  

