FROM phusion/baseimage:0.9.18  
MAINTAINER Safelink Internet  
# apache environment settings  
ENV DEBIAN_FRONTEND="noninteractive" HOME="/root" TERM="xterm"
APACHE_LOG_DIR="/var/log/apache2" APACHE_LOCK_DIR="/var/lock/apache2"
APACHE_PID_FILE="/var/run/apache2.pid"  
#Applying stuff  
RUN apt-get update && \  
apt-get install -y apache2 smokeping ssmtp && \  
rm /etc/ssmtp/ssmtp.conf && \  
ln -s /etc/smokeping/apache2.conf /etc/apache2/conf-available/apache2.conf &&
\  
a2enconf apache2 && \  
a2enmod cgid && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Adding Custom files  
ADD init/ /etc/my_init.d/  
ADD services/ /etc/service/  
ADD Alerts /tmp/Alerts  
ADD Database /tmp/Database  
ADD General /tmp/General  
ADD Presentation /tmp/Presentation  
ADD Probes /tmp/Probes  
ADD Slaves /tmp/Slaves  
ADD Targets /tmp/Targets  
ADD pathnames /tmp/pathnames  
ADD ssmtp.conf /tmp/ssmtp.conf  
ADD config /etc/smokeping/config  
RUN chmod -v +x /etc/service/*/run  
RUN chmod -v +x /etc/my_init.d/*.sh  
RUN mkdir /var/run/smokeping  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Volumes and Ports  
VOLUME /config  
VOLUME /data  
EXPOSE 80  

