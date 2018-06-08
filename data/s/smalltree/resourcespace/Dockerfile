FROM ubuntu:14.04  
MAINTAINER Keri Alleyne <info@symlogix.com>  
RUN apt-get update && apt-get install -y \  
antiword \  
apache2 \  
cron \  
ghostscript \  
imagemagick \  
libav-tools \  
libimage-exiftool-perl \  
mysql-server \  
nano \  
php5 \  
php5-dev \  
php5-gd \  
php5-mysql \  
postfix \  
subversion \  
vim \  
wget \  
xpdf  
RUN cd /var/www/html \  
&& svn co http://svn.montala.net/svn/resourcespace . \  
&& mkdir filestore \  
&& chmod 777 filestore \  
&& chmod -R 777 include  
RUN cp -a /etc/php5/apache2/php.ini /etc/php5/apache2/php.ini-original  
COPY php.ini /etc/php5/apache2/  
RUN /etc/init.d/mysql start \  
&& sleep 5 \  
&& mysql -uroot -e "create database resourcespace;"  
RUN mv /var/www/html/index.html /var/www/html/index.html-original  
  
  

