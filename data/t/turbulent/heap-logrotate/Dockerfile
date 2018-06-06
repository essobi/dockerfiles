FROM turbulent/heap-base:2.0.3  
ENV heap-logrotate 2.0.1  
MAINTAINER Benoit Beausejour <b@turbulent.ca>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get install -y memcached && \  
rm -rf /var/lib/apt/lists/*  
  
RUN rm /etc/logrotate.d/* && \  
rm -f /etc/cron.daily/* && \  
rm -f /etc/cron.weekly/* && \  
rm -f /etc/cron.monthly/* && \  
rm -f /etc/cron.d/*  
  
ADD run.sh /run.sh  
ADD logrotate.docker.tmpl /systpl/  
ADD logrotate.vol.tmpl /systpl/  
ADD cron.daily.logrotate.tmpl /systpl/  
ADD rsyslog-50-default.conf.tmpl /systpl/  
ADD supervisor.conf.tmpl /systpl/  
  
ENV LOGROTATE_MODE="daily" \  
LOGROTATE_ROTATE=7  
VOLUME ["/vol/logs", "/vol/docker-logs"]  
  
CMD ["/run.sh"]  

