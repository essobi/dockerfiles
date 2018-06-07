FROM ubuntu:14.04  
MAINTAINER Michael Tobby Sembiring <tsembiring@dyned.com>  
  
# Install apache, PHP, and supplimentary programs. openssh-server, curl, and
lynx-cur are for debugging the container.  
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive
apt-get -y install \  
apache2 php5 php5-mysql php5-curl php5-mcrypt libapache2-mod-php5 php5-cli
php5-common  
  
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
  
# Expose apache.  
EXPOSE 80  
# Copy this repo into place.  
ADD . /var/www/html/  
  
# Update the default apache site with the config we created.  
#ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
# By default start up apache in the foreground, override with /bin/bash for
interative.  
CMD /usr/sbin/apache2ctl -D FOREGROUND

