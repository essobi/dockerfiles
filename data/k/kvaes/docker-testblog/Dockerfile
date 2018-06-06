#  
# BlogTest Dockerfile  
#  
# Source : https://bitbucket.org/kvaes/docker-testblog/  
# Author : Karim Vaes  
#  
# Use Ubuntu 10.04 as a base  
FROM ubuntu:10.04  
# First let's do some updates!  
RUN apt-get update && apt-get -y upgrade  
  
# Install cron  
RUN apt-get -y install cron  
  
# Let's prep the directory  
RUN mkdir -p /data/bin  
  
# Pull the latest batch script  
ENV HOME /root  
COPY testblog.sh /data/bin/  
COPY testblogcron /data/bin/  
COPY startcron.sh /data/bin/  
  
# Setup 755 on the scripts  
RUN chmod 755 /data/bin/*.sh  
  
# Setup Cron Job  
RUN cat /data/bin/testblogcron >> /etc/crontab  
  
# Setup Cron Log  
RUN touch /var/log/testblog.log  
  
# Define default command.  
CMD ["/data/bin/startcron.sh"]  
  

