############################################################  
# Dockerfile to build prestashop apache-php container images  
# Based on phusion/baseimage  
############################################################  
# Set the base image to phusion/baseimage  
FROM phusion/baseimage:latest  
  
# File Author / Maintainer  
MAINTAINER Jonathan Temlett - Daedalus Solutions (jono@daedalus.co.za)  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for
debugging the container.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-
php5 php5-mysql php5-gd php-pear php-apc php5-curl curl lynx-cur  
  
#RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php5-json  
  
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
  
EXPOSE 80  
#EXPOSE 443  
  
# Install Prestashop  
RUN cd /tmp  
RUN apt-get install -y wget  
RUN wget http://www.prestashop.com/download/old/prestashop_1.6.1.2.zip  
RUN apt-get install -y unzip  
RUN unzip prestashop_1.6.1.2.zip -d /var/www/site/  
RUN chown -R www-data:www-data /var/www/site/  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Add the logic for page compression  
#ADD .htaccess /var/www/site/prestashop/.htaccess  
  
# By default, simply start apache.  
CMD /usr/sbin/apache2ctl -D FOREGROUND;  

