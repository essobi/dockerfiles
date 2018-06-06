FROM ubuntu:latest  
MAINTAINER <Harry Zhang : zh.harry@yahoo.ca>  
  
# Installs necesseary packages  
RUN apt-get update && \  
apt-get -y install \  
apache2 && \  
apt-get -y install \  
php7.0 \  
libapache2-mod-php7.0 && \  
apt-get -y install \  
php7.0-curl \  
php7.0-dev \  
php7.0-gd \  
php7.0-json \  
php7.0-mysql \  
php7.0-xml \  
php7.0-mbstring \  
php7.0-mcrypt && \  
apt-get -y install \  
php-pear \  
php-apcu && \  
apt-get -y install \  
libcurl4-openssl-dev \  
pkg-config \  
libssl-dev \  
libsslcommon2-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Installs and Enables PHP MongoDB driver  
RUN pecl install mongodb && \  
/bin/bash -c "echo extension=mongodb.so >> /etc/php/7.0/apache2/php.ini"  
# Set Apache Environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
# Copy modified apache2.conf into the configuration folder  
ADD apache2.conf /etc/apache2/apache2.conf  
  
# Enables Webpages  
RUN /usr/sbin/a2ensite default-ssl && \  
# Enables Apache2 Modules  
/usr/sbin/a2enmod ssl && \  
/usr/sbin/a2enmod rewrite  
  
# Listen to connections on 80 and 443  
EXPOSE 80  
EXPOSE 443  
# Start Apache  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

