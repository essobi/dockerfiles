FROM ubuntu:12.04  
MAINTAINER Florent Detry "florent@igloo.be"  
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
  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR && chown -R www-
data $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
  
RUN apt-get -qq update && apt-get install -y apache2 php5 php5-gd && \  
ln -sf /dev/stderr /var/log/apache2/error.log  
  
RUN a2enmod rewrite && a2enmod headers && a2enmod ssl  
  
EXPOSE 80 443  
CMD ["apache2", "-DFOREGROUND"]  

