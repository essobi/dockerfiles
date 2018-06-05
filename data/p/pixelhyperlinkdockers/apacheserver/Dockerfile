# PixelHyperlink Apache 2.4 Server Docker  
#  
# VERSION 1.1.0  
FROM pixelhyperlinkdockers/ubuntu:v1.8.0  
MAINTAINER Abhishek Salian <abhi@pixelhyperlink.com>  
  
LABEL Description="This image contains base ubuntu os with apache service."  
LABEL Vendor="PixelHyperlink"  
LABEL Version="1.1.0"  
LABEL com.pixelhyperlink.docker.apacheserver.version="1.1.0"  
LABEL vendor="PixelHyperlink"  
LABEL com.pixelhyperlink.docker.apacheserver.release-date="2017-07-05"  
LABEL com.pixelhyperlink.docker.apacheserver.version.is-production="true"  
  
ENV RUNLEVEL 1  
# Install apache.  
RUN add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install apache2 \  
apache2-doc \  
apache2-utils \  
libapache2-mod-fastcgi \  
libapache2-mod-mapcache \  
libapache2-mod-geoip \  
libapache2-mod-security2 \  
libapache2-mod-form \  
libapache2-mod-log-slow \  
libapache2-mod-xforward  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
  
# Expose apache.  
EXPOSE 80 443  
RUN mkdir -p /www/base_site && \  
chgrp -R www-data /www/base_site && \  
chmod -R g+w /www/base_site && \  
chmod g+s /www/base_site  
  
VOLUME ["/www/base_site", "/var/log/apache2"]  
  
# Copy apache config.  
COPY ./apache2.conf /etc/apache2/apache2.conf  
  
# Update the default apache site with the config we created.  
COPY ./000-default.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Set FQDN.  
COPY ./fqdn.conf /etc/apache2/conf-available/fqdn.conf  
  
# Copy server start up scripts  
COPY ./apache_entrypoint.sh /opt/apache_entrypoint.sh  
  
# Run startup scripts  
RUN chmod 777 /opt/apache_entrypoint.sh  
  
ENTRYPOINT ["/opt/apache_entrypoint.sh"]  

