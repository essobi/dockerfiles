FROM debian:jessie  
  
RUN apt-get update && apt-get install -y --no-install-recommends logrotate
cron \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LOGROTATE_PATHS=/var/log/*.log LOGROTATE_OPTIONS='rotate 72, dateext,
dateformat -%Y%m%d_%H%M%S, compress, missingok, notifempty, nocreate, su root
root'  
  
ADD start /start  
CMD ["/start"]  

