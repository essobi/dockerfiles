FROM mongo:3  
MAINTAINER gordon.burgett@gmail.com  
  
# install supporting services  
RUN apt-get update && apt-get install -y supervisor cron inotify-tools  
  
# copy scripts  
COPY tasks/ /tasks/  
  
# set up cron  
COPY cron-tasks /etc/cron.d/cron-tasks  
RUN chmod 0600 /etc/cron.d/cron-tasks && chmod 0700 /tasks/*  
  
# set up supervisor conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# create backup volume  
VOLUME /var/backup/  
  
# start by running supervisord  
ENTRYPOINT ["/usr/bin/supervisord"]

