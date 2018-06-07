############################################################  
# Dockerfile to build prestashop apache-php container images  
# Based on phusion/baseimage  
############################################################  
# Set the base image to phusion/baseimage  
FROM phusion/baseimage:latest  
CMD ["/sbin/my_init"]  
  
# File Author / Maintainer  
MAINTAINER Jonathan Temlett - Daedalus Solutions (jono@daedalus.co.za)  
  
RUN apt-add-repository -y ppa:ondrej/php  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for
debugging the container.  
#RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-
php5 php5-mysql php-soap php5-gd php-pear php-apc php5-curl curl lynx-cur
php5-mcrypt  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apache2 \  
libapache2-mod-php5.6 \  
php5.6 \  
curl \  
lynx-cur  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \  
php5.6-gd \  
php5.6-apc \  
php5.6-mysql \  
php5.6-dom \  
php5.6-cli \  
php5.6-json \  
php5.6-common \  
php5.6-mbstring \  
php5.6-opcache \  
php5.6-readline \  
php5.6-curl \  
php5.6-mcrypt \  
php5.6-soap \  
php5.6-zip  
  
#RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php5-json  
  
# Enable apache mods.  
RUN a2enmod php5.6  
RUN a2enmod rewrite  
RUN update-alternatives --set php /usr/bin/php5.6  
  
# Update the PHP.ini file, enable <? ?> tags and quieten logging.  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php/5.6/apache2/php.ini  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php/5.6/apache2/php.ini  
RUN sed -i "s/^upload_max_filesize.*/upload_max_filesize = 256M/"
/etc/php/5.6/apache2/php.ini  
RUN sed -i "s/^post_max_size.*/post_max_size = 256M/"
/etc/php/5.6/apache2/php.ini  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
EXPOSE 80  
RUN mkdir /var/www/site  
RUN chown -R www-data:www-data /var/www/site/  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# By default, simply start apache.  
CMD /usr/sbin/apache2ctl -D FOREGROUND;  

