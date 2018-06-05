FROM ubuntu:16.04  
MAINTAINER Mark Oliver <mark@oliver.cx>  
  
# Password for mysql  
ENV MYSQLPASSWORD password  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
# Install apache, PHP, and supplimentary programs. openssh-server, curl, and
lynx-cur are for debugging the container.  
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive
apt-get -y install \  
apache2 php7.0 php7.0-mysql libapache2-mod-php7.0 curl lynx-cur  
  
# Enable apache mods.  
RUN a2enmod php7.0  
RUN a2enmod rewrite  
  
# Install Mysql  
RUN echo mysql-server mysql-server/root_password password $MYSQLTMPROOT |
debconf-set-selections;\  
echo mysql-server mysql-server/root_password_again password $MYSQLTMPROOT |
debconf-set-selections;\  
apt-get install -y mysql-server mysql-client libmysqlclient-dev  
  
# Update the PHP.ini file, shush logging.  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php/7.0/apache2/php.ini  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
# Expose apache.  
EXPOSE 80  
# Copy this repo into place.  
ADD www /var/www/oliver  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Clean up APT and bundler when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# By default start up apache in the foreground, override with /bin/bash for
interative.  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

