  
FROM ubuntu  
  
MAINTAINER levm "av@levm.eu"  
# Install the relevant packages  
RUN apt-get update && apt-get install apache2 libapache2-mod-php php-mysql -y  
  
# Enable the php mod we just installed  
RUN a2enmod php7.0 rewrite  
  
# Update our apache sites available with the config we created  
ADD hotglue-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Manually set the apache environment variables in order to get apache to work
immediately.  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE=/var/run/apache2.pid  
ENV APACHE_PID_FILE=/var/run/apache2.pid  
ENV APACHE_LOCK_DIR=/var/lock/apache2  
ENV APACHE_RUN_DIR=/var/run/apache2  
  
# Execute the apache daemon in the foreground so we can treat the container as
an  
# executeable and it wont immediately return.  
EXPOSE 80  
EXPOSE 443  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
  

