FROM debian:jessie  
MAINTAINER Jean-Avit Promis "docker@katagena.com"  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install subversion apache2
libapache2-mod-php5 wget unzip php5-dev php5-mcrypt php5-curl php5-pgsql
php5-mysql php5-sqlite php5-mongo php5-memcached php5-xdebug php-apc
php5-imagick php5-gd php5-geoip gcc git libpcre3-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget https://github.com/phalcon/cphalcon/archive/phalcon-v2.0.10.zip && \  
unzip phalcon-v2.0.10.zip -d /usr/local/src/cphalcon && \  
cd /usr/local/src/cphalcon/cphalcon-phalcon-v2.0.10/build && ./install ;\  
echo "extension=phalcon.so" > /etc/php5/mods-available/phalcon.ini ;\  
php5enmod phalcon  
  
RUN a2enmod rewrite  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid  
  
ADD 000-default.conf /etc/apache2/sites-available/000-default.conf  
RUN a2ensite 000-default  
  
RUN wget --no-check-certificate
https://github.com/rmccue/Requests/archive/v1.6.0.zip && \  
unzip v1.6.0.zip && \  
cp Requests-1.6.0/library/Requests.php /usr/share/php/ && \  
cp -R Requests-1.6.0/library/Requests/ /usr/share/php/ && \  
wget http://www.meekro.com/download.php && \  
mv download.php /usr/share/php/meekrodb.class.php  
  
RUN echo "<?php phpinfo();?>" > /var/www/index.php  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
EXPOSE 80  
CMD /start.sh  

