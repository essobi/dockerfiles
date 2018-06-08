#name of container: docker-openemr  
#versison of container: 0.3.2  
FROM quantumobject/docker-baseimage:16.04  
MAINTAINER Angel Rodriguez "angel@quantumobject.com"  
# Update the container  
# Installation of nesesary package/software for this containers...  
RUN apt-get update && apt-get install -y -q apache2 \  
php7.0 \  
libapache2-mod-php7.0 \  
libdate-calc-perl \  
libdbd-mysql-perl \  
libhtml-parser-perl \  
libdbi-perl \  
libwww-mechanize-perl \  
libxml-parser-perl \  
libtiff-tools \  
php7.0-mysql \  
php7.0-cli \  
php7.0-gd \  
php7.0-xsl \  
php7.0-curl \  
php7.0-mcrypt \  
php7.0-soap \  
imagemagick \  
php7.0-json \  
php7.0-mbstring \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
#General variable definition....  
##startup scripts  
COPY php.ini /etc/php/7.0/apache2/php.ini  
COPY apache2.conf /etc/apache2/apache2.conf  
  
#Pre-config scrip that maybe need to be run one time only when the container
run the first time .. using a flag to don't  
#run it again ... use for conf for service ... when run the first time ...  
RUN mkdir -p /etc/my_init.d  
COPY startup.sh /etc/my_init.d/startup.sh  
RUN chmod +x /etc/my_init.d/startup.sh  
  
# to add apache2 deamon to runit  
RUN mkdir -p /etc/service/apache2 /var/log/apache2 ; sync  
COPY apache2.sh /etc/service/apache2/run  
RUN chmod +x /etc/service/apache2/run \  
&& cp /var/log/cron/config /var/log/apache2/ \  
&& chown -R www-data /var/log/apache2  
  
#pre-config scritp for different service that need to be run when container
image is create  
#maybe include additional software that need to be installed ... with some
service running ... like example mysqld  
COPY pre-conf.sh /sbin/pre-conf  
RUN chmod +x /sbin/pre-conf ; sync \  
&& /bin/bash -c /sbin/pre-conf \  
&& rm /sbin/pre-conf  
  
#backup or keep data integrity ..  
##scritp that can be running from the outside using docker exec tool ...  
COPY backup.sh /sbin/backup  
RUN chmod +x /sbin/backup  
VOLUME /var/backups  
  
#add files and script that need to be use for this container  
#include conf file relate to service/daemon  
#script to execute after install configuration done ....  
COPY after_install.sh /sbin/after_install  
RUN chmod +x /sbin/after_install  
  
EXPOSE 80  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

