# build  
# docker build . -t gitback  
# run (prd)  
# docker run -ti -e DATABASE_URL=xxxxxxxx -p 443:443 -v /git:/git -v
$(pwd)/ssl:/etc/ssl/private gitback  
# run (dev)  
# docker run -ti -e DATABASE_URL=postgresql://hp@192.168.178.20/riseml -p
1234:443 -v $(pwd)/git:/git -v $(pwd)/ssl:/etc/ssl/private gitback  
FROM ubuntu:16.04  
RUN apt-get -y update --fix-missing && \  
apt-get -y install git apache2 libaprutil1-dbd-pgsql  
  
ENV APACHE_RUN_DIR /var/run  
ENV APACHE_LOCK_DIR /var/lock  
ENV APACHE_SERVERADMIN admin@localhost  
ENV APACHE_SERVERNAME localhost  
ENV SSL 1  
ENV PORT 443  
EXPOSE 80  
EXPOSE 443  
ENV DATABASE_URL postgresql:///riseml  
ENV GIT_ROOT /git  
  
RUN usermod -u 1000 www-data && \  
groupmod -g 1000 www-data && \  
a2enmod ssl env alias cgid authn_dbd rewrite && \  
a2dismod mpm_* && \  
rm /usr/share/apache2/default-site/index.html && \  
rm /var/www/html/index.html  
  
COPY apache2.conf /etc/apache2/apache2.conf  
  
CMD if [ "$SSL" -eq "1" ]; then \  
chown www-data:www-data /git && \  
/usr/sbin/apache2 -D FOREGROUND -D ENABLE_SSL; \  
else \  
chown www-data:www-data /git && \  
/usr/sbin/apache2 -D FOREGROUND; \  
fi  

