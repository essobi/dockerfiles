FROM gordinlearninglayers/backup  
  
# add all files from conf subfolder to conf data volume  
ADD conf/ /usr/local/etc/openldap/  
  
# Create a database folder  
RUN mkdir /usr/local/etc/openldap/openldap-data  
  
# provide directories conf and logs as volumes  
VOLUME ["/usr/local/etc/openldap", "/backup-scripts/"]  
  
# add restore script for backups  
ADD restore.sh /backup-scripts/restore.sh  
ADD backup.sh /backup-scripts/backup.sh  
  
CMD ["/backup-scripts/restore.sh"]  

