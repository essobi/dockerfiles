FROM ubuntu:latest  
MAINTAINER Özgün Çağrı AYDIN <ozguncagri@gmail.com>  
  
# Install Apache 2, PHP 7 and some modules for development  
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive
apt-get -y install \  
apache2 \  
php7.0 \  
libapache2-mod-php7.0 \  
curl \  
php7.0-mysql \  
php7.0-pgsql \  
php7.0-sqlite3 \  
php7.0-mbstring \  
php7.0-curl \  
php7.0-mcrypt \  
php7.0-bz2 \  
php7.0-gd \  
php7.0-bcmath \  
php7.0-xml \  
php7.0-zip \  
php-redis \  
php-mongodb \  
php-imagick  
  
# Enable apache mods.  
RUN a2enmod php7.0  
RUN a2enmod rewrite  
  
# Suppress FQDN message  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
# Expose apache to world  
EXPOSE 80  
# Copy www folder to app folder  
ADD www /var/www  
  
# Update default apache site with our config  
ADD apache-config.conf /etc/apache2/sites-enabled/000-default.conf  
  
# Start apache in the foreground (you can override it with /bin/bash)  
CMD /usr/sbin/apache2ctl -D FOREGROUND

