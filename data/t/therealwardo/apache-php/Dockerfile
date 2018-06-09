FROM ubuntu:12.04  
  
MAINTAINER Matt Ward  
  
RUN \  
apt-get update && \  
apt-get install -y \  
apache2 \  
libapache2-mod-php5 \  
php5 \  
php5-cli \  
php5-common \  
php5-curl \  
php5-dev \  
php5-gd \  
php5-gmp \  
php5-mcrypt \  
php5-memcache \  
php5-mysql \  
php5-xsl \  
php-apc \  
php-pear \  
python-mysqldb  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 80  
  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

