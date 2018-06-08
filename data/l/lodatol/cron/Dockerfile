FROM busybox  
  
RUN mkdir -p /var/spool/cron/crontabs  
  
CMD ntpd -p pool.ntp.org && echo "$CRON_ENTRY" | crontab - && crond -f  

