FROM debian:jessie  
  
RUN apt-get update -y && apt-get install -y software-properties-common  
  
RUN add-apt-repository -y "deb http://ftp.us.debian.org/debian stable non-
free"  
RUN add-apt-repository -y "deb http://ftp.us.debian.org/debian jessie-updates
non-free"  
RUN add-apt-repository -y "deb http://security.debian.org/ jessie/updates non-
free"  
  
RUN apt-get update -y && apt-get install -y \  
acl \  
curl \  
python-software-properties \  
apache2-mpm-prefork \  
# libapache2-mod-fastcgi \  
libapache2-mod-upload-progress  
  
ENV APACHE_LOCK_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN a2dismod mpm_event  
  
RUN a2enmod \  
actions \  
expires \  
headers \  
mpm_prefork \  
proxy \  
proxy_fcgi \  
reqtimeout \  
rewrite \  
vhost_alias  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]

