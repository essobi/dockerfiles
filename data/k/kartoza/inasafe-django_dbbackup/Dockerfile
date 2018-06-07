FROM kartoza/pg-backup:9.6  
MAINTAINER tim@kartoza.com  
  
# Add cronjob overrides to customize backup time trigger  
ADD backups-cron /etc/cron.d/backups-cron  
ADD backups.sh /backups.sh  
  
ENTRYPOINT /start.sh  

