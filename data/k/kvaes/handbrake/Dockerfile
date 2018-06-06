#  
# Handbrake Dockerfile  
#  
# Source : https://bitbucket.org/kvaes/docker-handbrake/  
# Author : Karim Vaes  
#  
# Use Ubuntiu 10.04 as a base  
FROM ubuntu:10.04  
# Add Handbrake Repository  
RUN echo "deb http://ppa.launchpad.net/stebbins/handbrake-releases/ubuntu
lucid main" >> /etc/apt/sources.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 816950D8  
  
# First let's do some updates!  
RUN apt-get update && apt-get -y upgrade  
  
# Install handbrake-cli, cron & Mercurial  
RUN apt-get -y install cron handbrake-cli  
  
# Let's prep the handbrake install  
RUN mkdir -p /data/bin && mkdir -p /data/in && mkdir -p /data/out && mkdir -p
/data/temp  
  
# Pull the latest handbrake batch script  
ENV HOME /root  
COPY handbrake.sh /data/bin/  
COPY handbrakecron /data/bin/  
  
# Setup 755 on handbrake.sh  
RUN chmod 755 /data/bin/handbrake.sh  
  
# Setup Cron Job  
RUN cat /data/bin/handbrakecron >> /etc/crontab  
  
# Setup Cron Log  
#RUN touch /var/log/handbrake.log  
# Setup Cron Entrypoint  
ENTRYPOINT ["cron"]  
  
# Setup Volumes  
VOLUME ["/data/in"]  
VOLUME ["/data/temp"]  
VOLUME ["/data/out"]  
  
# Define default command.  
CMD ["cron", "-f"]  

