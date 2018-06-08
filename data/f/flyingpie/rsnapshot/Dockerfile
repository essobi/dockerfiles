FROM ubuntu:14.04  
MAINTAINER Marco vd Oever <marco@flyingpie.nl>  
  
RUN apt-get update && apt-get install -y \  
rsnapshot  
  
COPY ./rsnapshot.conf /etc/rsnapshot.conf  
COPY ./crontab /crontab  
  
RUN touch /var/log/cron.log  
  
RUN crontab crontab  
  
VOLUME /source  
VOLUME /target  
  
CMD rsyslogd && cron && tail -f /var/log/syslog /var/log/cron.log  

