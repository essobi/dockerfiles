# Dockerfile for konrad54/mariadb-encrypted-backup  
FROM mariadb:10.1.14  
  
MAINTAINER Konrad Biedowicz <konrad.biedowicz@uni-greifswald.de>  
  
COPY entry.sh /entry.sh  
COPY db-backups.sh /scripts/db-backups.sh  
COPY db-restore.sh /scripts/db-restore.sh  
  
ENV BACKUP_DIR=/backup  
  
RUN apt-get update && apt-get install -y cron && \  
chmod +x /entry.sh && \  
chmod +x /scripts/db-backups.sh && \  
chmod +x /scripts/db-restore.sh  
  
CMD ["/entry.sh"]  

