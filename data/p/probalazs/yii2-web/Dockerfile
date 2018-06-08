# yii2-web  
#  
# VERSION 1.0.0  
  
FROM ubuntu:14.04  
  
MAINTAINER probalazs <probalazs@nyenyere.eu>  
  
RUN apt-get update && apt-get install -y apache2 \  
curl \  
php5 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-curl \  
php5-gd \  
php5-intl \  
php-pear \  
php5-imagick \  
php5-imap \  
php5-mcrypt \  
php5-memcache \  
php5-ming \  
php5-ps \  
php5-pspell \  
php5-recode \  
php5-snmp \  
php5-sqlite \  
php5-tidy \  
php5-xmlrpc \  
php5-xsl \  
mcrypt  
  
RUN php5enmod mcrypt  
RUN a2enmod rewrite  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

