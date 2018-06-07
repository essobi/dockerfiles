FROM ubuntu:latest  
#!/bin/bash  
MAINTAINER Dan Pupius <dan@pupi.us>  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for
debugging the container.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-
php5 php5-mysql php5-gd php-pear php-apc php5-curl curl lynx-cur  
  
# Enable apache mods.  
RUN a2enmod php5  
RUN a2enmod rewrite  
  
# Update the PHP.ini file, enable <? ?> tags and quieten logging.  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php5/apache2/php.ini  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php5/apache2/php.ini  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
#Config date  
RUN yes | cp /usr/share/zoneinfo/America/Bogota /etc/localtime  
  
# Expose the ports we're interested in  
EXPOSE 80  
EXPOSE 443  
# Copy site into place.  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
RUN adduser --system --uid=1000 staff  
RUN sed -i -- 's/export APACHE_RUN_USER=www-data/export
APACHE_RUN_USER=staff/g' /etc/apache2/envvars  
RUN sed -i -- 's/export APACHE_RUN_GROUP=www-data/export
APACHE_RUN_GROUP=staff/g' /etc/apache2/envvars  
RUN apt-get install nano  
  
# By default, simply start apache.  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

