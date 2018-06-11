FROM ubuntu:14.04  
MAINTAINER Jefim Borissov  
RUN \  
apt-get update && \  
#apt-get upgrade -y && \  
apt-get install -y apache2 && \  
apt-get install -y php5 libapache2-mod-php5 php5-mcrypt php5-mysql && \  
apt-get install -y php5-gd php-pear php-apc php5-curl curl && \  
apt-get install -y mysql-client && \  
a2enmod rewrite && \  
a2enmod php5 && \  
service apache2 stop  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
ADD www /var/www/site  
ADD htaccess /var/www/site/.htaccess  
  
# Update the default apache site with the config we created.  
ADD apache.conf /etc/apache2/sites-enabled/000-default.conf  
  
EXPOSE 80  
  
ADD init.sh /init.sh  
RUN chmod +x /init.sh  
ENTRYPOINT ["/init.sh"]

