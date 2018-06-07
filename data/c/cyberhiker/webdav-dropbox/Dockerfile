FROM ubuntu:16.10  
MAINTAINER Chris Burton <cyberhiker@gmail.com>  
  
# Create service account and set permissions.  
RUN groupadd dropbox \  
&& useradd -m -d /dbox -c "Dropbox Daemon Account" -s /usr/sbin/nologin -g
dropbox dropbox  
  
RUN apt-get update && \  
apt-get install -y apache2 apache2-utils && \  
apt-get autoremove -y  
  
RUN mkdir -p /opt/.dropbox /opt/.dropbox-dist /opt/Dropbox /opt/base  
  
# Install init script and dropbox command line wrapper  
COPY run /root/  
COPY dropbox /usr/bin/dropbox  
COPY webdav.conf /etc/apache2/sites-available/webdav.conf  
  
# Enable Web DAV  
RUN a2enmod dav dav_fs  
RUN a2dissite 000-default  
RUN a2ensite webdav  
  
ENV APACHE_RUN_USER dropbox  
ENV APACHE_RUN_GROUP dropbox  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_RUN_DIR /var/run/apache2  
  
RUN mkdir -p /var/lock/apache2; chown dropbox /var/lock/apache2  
  
EXPOSE 8888  
VOLUME ["/dbox/.dropbox", "/dbox/Dropbox"]  
  
WORKDIR /dbox/Dropbox  
EXPOSE 17500  
ENTRYPOINT ["/root/run"]  

