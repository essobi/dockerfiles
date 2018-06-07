FROM gordinlearninglayers/backup  
  
MAINTAINER István Koren  
  
VOLUME ["/var/lib/mysql/", "/backup-scripts"]  
  
ADD restore.sh /backup-scripts/restore.sh  
ADD backup.sh /backup-scripts/backup.sh  
  
CMD ["/backup-scripts/restore.sh"]  

