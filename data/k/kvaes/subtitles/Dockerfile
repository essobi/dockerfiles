#  
# Handbrake Dockerfile  
#  
# Source : https://bitbucket.org/kvaes/docker-subtitles/  
# Author : Karim Vaes  
#  
# Use Ubunut 10.04 as a base  
FROM ubuntu:10.04  
# First let's do some updates!  
RUN apt-get update && apt-get -y upgrade  
  
# Install wget, python-setuptools, cron  
RUN apt-get -y install cron python-setuptools wget  
  
# Install argparse  
RUN easy_install argparse  
  
# Let's prep the subtitles install  
RUN mkdir -p /data/bin && mkdir -p /data/in  
  
# Pull the latest subtitle script  
ENV HOME /root  
COPY OpenSubtitlesDownload.py /data/bin/  
COPY subtitlescron /data/bin/  
  
# Setup 755 on OpenSubtitlesDownload.py  
RUN chmod 755 /data/bin/OpenSubtitlesDownload.py  
  
# Setup Cron Job  
RUN cat /data/bin/subtitlescron >> /etc/crontab  
  
# Setup Cron Log  
RUN touch /var/log/subtitles.log  
  
# Setup Cron Entrypoint  
ENTRYPOINT ["cron"]  
  
# Setup Volumes  
VOLUME ["/data/in"]  
  
# Define default command.  
CMD ["cron", "-f"]  

