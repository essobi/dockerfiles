FROM ubuntu:xenial  
  
ENV MAX_BACKUPS=7 \  
CRON_TIME="0 0 * * *" \  
BACKUP_FILE_PREFIX="jenkins-backup"  
VOLUME ["/var/jenkins_home", "/var/backups"]  
  
RUN apt-get update && apt-get install -y cron  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  

