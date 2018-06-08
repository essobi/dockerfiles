FROM ubuntu:latest  
MAINTAINER Jiri Kratochvil <jiri.kratochvil@topmonks.com>  
  
RUN apt-get -y install rsync cron  
  
WORKDIR /tmp  
ADD . /tmp  
  
# Add crontab file in the cron directory  
ADD crontab /etc/cron.d/backup-cron  
  
RUN touch /var/log/cron.log  
RUN chmod 0644 /etc/cron.d/backup-cron  
  
CMD env > /root/env.txt && cron && tail -f /var/log/cron.log

