# DOCKER-VERSION 0.3.4  
FROM spiritdev/ubuntu  
MAINTAINER Jean Bordat <bordat.jean@gmail.com>  
  
# Install Apache2  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 libapache2-mod-
php5 php5-imagick php5-gd php5-intl php5-mcrypt php5-apcu php5-curl php5-mysql
acl  
  
# Modify PHP session directory for Apache2  
COPY ./php.conf.d /etc/php5/apache2/conf.d/  
  
# Enable rewrite module  
RUN a2enmod rewrite  
  
# Configure Apache2  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
env APACHE_PID_FILE /var/run/apache2.pid  
env APACHE_RUN_DIR /var/run/apache2  
env APACHE_LOCK_DIR /var/lock/apache2  
env APACHE_LOG_DIR /var/log/apache2  
  
# Remove default VirtualHost  
RUN rm -rf /etc/apache2/sites-enabled/000-default.conf  
RUN rm -rf /var/www/html  
  
# Expose port.  
EXPOSE 80

