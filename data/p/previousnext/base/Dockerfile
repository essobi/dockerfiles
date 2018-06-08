# This is a base container for PNX docker containers.  
FROM ubuntu:12.04  
MAINTAINER Nick Schuch <nick@previousnext.com.au>  
  
##  
# APT.  
##  
RUN apt-get update  
RUN apt-get -y dist-upgrade  
  
# Keep upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -fs /bin/true /sbin/initctl  
  
##  
# Base.  
##  
# APT.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install fail2ban vim git curl
wget pwgen python-setuptools vim-tiny sudo python-software-properties cron
unzip  
  
# Ensure that locale files are regenerated.  
RUN locale-gen en_AU en_AU.UTF-8  
RUN dpkg-reconfigure locales  
  
##  
# Users.  
##  
RUN useradd --create-home --shell /bin/bash --user-group deployer  
  
##  
# SSHD.  
##  
RUN apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd  
  
##  
# Fail2ban.  
##  
RUN mkdir /var/run/fail2ban  
  
##  
# Rsyslog.  
##  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install rsyslog rsyslog-doc  
RUN sed -i 's/xconsole/console/g' /etc/rsyslog.d/*  
  
##  
# Startup scripts.  
##  
ADD ./scripts/start.sh /root/start.sh  
RUN chmod 755 /root/start.sh  
  
##  
# Supervisord.  
##  
RUN easy_install supervisor  
ADD ./conf/supervisor/supervisord.conf /etc/supervisord.conf  
RUN mkdir /var/log/supervisor/  
  
##  
# Inotify  
##  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y autoremove  
  
# Cleanup.  
RUN apt-get -y dist-upgrade  

