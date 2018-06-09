FROM ubuntu:14.04  
MAINTAINER Paul Velez "paul@relayrides.com"  
# Install apache  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -y && \  
apt-get install -y apache2=2.4.7-1ubuntu4.5  
  
# let's copy a few of the settings from /etc/init.d/apache2  
ENV APACHE_CONFDIR /etc/apache2  
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars  
# and then a few more from $APACHE_CONFDIR/envvars itself  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_PID_FILE $APACHE_RUN_DIR/apache2.pid  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV LANG C  
  
# ...  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
  
RUN a2enmod rewrite proxy proxy_http ssl headers  
  
COPY apache2-foreground /usr/local/bin/  
RUN chmod a+x /usr/local/bin/apache2-foreground  
  
EXPOSE 443  
VOLUME ["/data", "/etc/apache2/sites-available", "/etc/apache2/sites-enabled",
"/etc/apache2/ssl", "/var/www/resources", "/var/www/media"]  
CMD ["apache2-foreground"]  

