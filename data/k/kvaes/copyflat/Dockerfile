#  
# CopyFlat Dockerfile  
#  
# Source : https://bitbucket.org/kvaes/docker-copyflat/  
# Author : Karim Vaes  
#  
# Use Ubunut 10.04 as a base  
FROM ubuntu:10.04  
# First let's do some updates!  
RUN apt-get update && apt-get -y upgrade  
  
# Install cron  
RUN apt-get -y install cron  
  
# Let's prep the install  
RUN mkdir -p /data/bin && mkdir -p /data/in && mkdir -p /data/out  
  
# Pull the latest batch script  
ENV HOME /root  
COPY copyflat.sh /data/bin/  
COPY copyflatcron /data/bin/  
COPY startcron.sh /data/bin/  
  
# Setup 755 on scripts  
RUN chmod 755 /data/bin/*.sh  
  
# Setup Cron Job  
RUN cat /data/bin/copyflatcron >> /etc/crontab  
  
# Setup Cron Log  
RUN touch /var/log/copyflat.log  
  
# Setup Volumes  
VOLUME ["/data/in"]  
VOLUME ["/data/out"]  
  
# Define default command.  
CMD ["/data/bin/startcron.sh"]  

