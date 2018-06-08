FROM ubuntu:latest  
  
MAINTAINER Kerry Knopp <krknopp@gmail.com>  
  
# Install cron and supervisor  
RUN apt-get update && apt-get install -y supervisor cron git curl ca-
certificates \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
# copy in supervisord config  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Remove cron.* directories  
RUN rm -Rf /etc/cron.daily /etc/cron.weekly /etc/cron.monthly /etc/cron.hourly  
  
#Add crontab and logger script  
COPY crontab /etc/crontab  
COPY logger.sh /bin/logger.sh  
COPY make_symlinks.sh /opt/make_symlinks.sh  
  
# Add scripts folder  
RUN mkdir /opt/scripts  
RUN touch /var/log/syslog  
  
# Add the run script  
ADD run.sh /opt/run.sh  
  
# Default script  
CMD ["/opt/run.sh"]  

