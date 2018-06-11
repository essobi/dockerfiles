FROM ubuntu:latest  
  
MAINTAINER Tyler McHenry <tyler.mchenry@gmail.com>  
  
# Install cron and supervisor  
RUN apt-get update  
RUN apt-get install cron -yqq  
RUN apt-get install supervisor -yqq  
RUN apt-get install rsyslog -yqq  
RUN apt-get install curl -yqq  
RUN apt-get install run-one -yqq  
RUN apt-get install ssh -yqq  
RUN apt-get install rsync -yqq  
RUN apt-get install inotify-tools -yqq  
RUN apt-get install ffmpeg -yqq  
RUN apt-get install ttf-dejavu -yqq  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Remove cron.* directories  
RUN rm -Rf /etc/cron.daily  
RUN rm -Rf /etc/cron.weekly  
RUN rm -Rf /etc/cron.monthly  
RUN rm -Rf /etc/cron.hourly  
  
#Add crontab and logger script  
COPY crontab /etc/crontab  
COPY logger.sh /bin/logger.sh  
  
# Add the run script  
ADD run.sh /opt/run.sh  
RUN chmod 700 /opt/run.sh  
  
# Default script  
CMD ["/opt/run.sh"]  

