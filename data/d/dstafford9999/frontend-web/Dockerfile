FROM ubuntu:16.04  
# Add hosts entry  
RUN echo "127.0.0.1 einsteinplano.com" >> /etc/hosts  
  
# Install apache, PHP, and supplimentary programs. openssh-server, curl, and
lynx-cur are for debugging the container.  
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive
apt-get -y install \  
apache2 php7.0 php7.0-mysql php7.0-intl libapache2-mod-php7.0 curl lynx-cur
php7.0-xml php7.0-zip php7.0-curl php7.0-gd \  
wget pwgen python-setuptools curl unzip cifs-utils sendmail php7.0-mbstring  
  
# Enable apache mods.  
RUN a2enmod php7.0  
RUN a2enmod rewrite  
  
# Update the PHP.ini file, enable <? ?> tags and quieten logging.  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php/7.0/apache2/php.ini  
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
# Create folders  
RUN mkdir /var/www/uploads  
RUN mkdir /var/www/moodledata  
RUN mkdir /var/www/core  
  
# Copy .htaccess  
# ADD .htaccess /var/www/core  
# Copy config.php  
# ADD config.php /var/www/core  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Set permissions of all site files so they are not publicly writeable  
RUN chmod -R 755 /var/www/core  
RUN chown -R www-data:www-data /var/www/core  
RUN chmod -R 766 /var/www/uploads  
RUN chown -R www-data:www-data /var/www/uploads  
RUN chmod -R 766 /var/www/moodledata  
RUN chown -R www-data:www-data /var/www/moodledata  
  
# Cleanup, this is ran to reduce the resulting size of the image.  
RUN apt-get clean autoclean && apt-get autoremove -y && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/* /var/lib/dpkg/* /var/lib/cache/*
/var/lib/log/*  
  
# By default start up apache in the foreground, override with /bin/bash for
interactive.  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

