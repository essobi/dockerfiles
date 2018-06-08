##############################################  
# Dockerfile to build Apache HTTP server image  
##############################################  
# Base image  
FROM ubuntu:16.04  
  
# Author: MobileSnapp Inc.  
MAINTAINER MobileSnapp <support@mobilesnapp.com>  
  
# Install Apache HTTP server  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y \  
apache2 \  
curl && \  
apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
# Install PHP and helper packages  
RUN apt-get update && \  
apt-get dist-upgrade -y && \  
apt-get install -y \  
php7.0 \  
libapache2-mod-php7.0 \  
php7.0-mysql \  
php7.0-curl \  
php7.0-json \  
&& apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
/usr/share/doc/*  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
# Assign working directory  
WORKDIR /var/www/site/  
  
# Expose web and SSL ports.  
EXPOSE 80  
EXPOSE 443  
  
# Update the default apache site with the config we created.  
ADD apache-config.conf /etc/apache2/sites-available/000-default.conf  
  
# Resolving host  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Enable site  
RUN a2ensite 000-default  
  
ADD dir.conf /etc/apache2/mods-enabled/dir.conf  
  
# Activate mod_rewrites  
RUN a2enmod rewrite  
  
# Restart server  
RUN service apache2 restart  
  
RUN apt-get update && apt-get install -y \  
libpq-dev \  
libmemcached-dev \  
curl \  
libpng12-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
\--no-install-recommends \  
&& rm -r /var/lib/apt/lists/*  
  
# By default start up apache in the foreground, override with /bin/bash for
interative.  
CMD /usr/sbin/apache2ctl -D FOREGROUND

