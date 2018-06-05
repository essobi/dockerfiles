FROM ubuntu:14.04  
ENV APACHE_UID 33  
ENV APACHE_GID 33  
ENV APACHE_RUN_USER #${APACHE_UID}  
ENV APACHE_RUN_GROUP #${APACHE_GID}  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_PORT 80  
RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -rf
/var/lib/apt/lists/*  
RUN a2enmod dav dav_fs  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
RUN mkdir -p /var/lock/apache2; chown $APACHE_UID /var/lock/apache2  
RUN sed -i 's/Listen 80/Listen ${APACHE_PORT}/' /etc/apache2/ports.conf  
  
ADD webdav.conf /etc/apache2/sites-enabled/webdav.conf  
ADD run.sh /run.sh  
  
VOLUME ["/srv/webdav"]  
EXPOSE $APACHE_PORT  
  
CMD ["bash", "-x", "/run.sh"]  

