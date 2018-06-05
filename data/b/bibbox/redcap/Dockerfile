FROM ubuntu:trusty  
MAINTAINER Lukas Pessl <lukas.pessl@medunigraz.at>  
  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install packages  
RUN apt-get update && \  
apt-get -y install supervisor \  
git \  
apache2 \  
libapache2-mod-php5 \  
mysql-server \  
php5-mysql \  
pwgen \  
php-apc \  
phpmyadmin \  
php5-curl \  
php5-gd \  
php5-mcrypt \  
nano \  
ssmtp \  
&& \  
echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Set LOG Directories  
RUN mkdir /var/log/export && chgrp adm /var/log/export  
  
# Add image configuration and scripts  
ADD start-apache2.sh /start-apache2.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Configure supervisord to manage processes (otherwise a docker instance can
only run 1 process)  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
ADD supervisord-cron.conf /etc/supervisor/conf.d/supervisord-cron.conf  
  
# config to enable .htaccess  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
# Add readme as a dummy html file in case someone forgets to map the
redcap_webroot  
# ADD README.md /var/www/html/index.html  
# enable mcrypt  
RUN php5enmod mcrypt  
  
# Configure /redcap_webroot as the webfolder  
# RUN git clone https://github.com/fermayo/hello-world-lamp.git /app  
# RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
# RUN mkdir -p /redcap_webroot && rm -fr /var/www/html && ln -s
/redcap_webroot /var/www/html  
# Make a link from /redcap_webroot to the real webroot. This makes the mapped
folder  
RUN ln -s /var/www/html /redcap_webroot  
  
RUN chown -R www-data:www-data /var/www/html  
  
#Environment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 32M  
ENV PHP_POST_MAX_SIZE 32M  
  
# You must escape the / with a blackslash  
ENV PHP_TIMEZONE "America\/Los_Angeles"  
# Recommended by REDCap  
ENV PHP_MAX_INPUT_VARS 10000  
# What directory in the mounted redcap_webroot folder does redcap reside in -
should be "/" or "/redcap/" in most cases...  
# This is used to set the cron task  
ENV PHP_REDCAP_FOLDER "/"  
# Assumes REDCap is one dir down  
# ENV PHP_CRON_COMMAND "php /redcap_webroot/cron.php"  
# Add mappable volumes  
VOLUME [ "/redcap_webroot", "/var/log/export" ]  
  
EXPOSE 80 3306 8025  
CMD ["/run.sh"]  

