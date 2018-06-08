# Base image  
FROM alpine:edge  
  
RUN apk add --no-cache postgresql  
  
# Create folder for database backup  
RUN mkdir -p /var/backups/db  
  
VOLUME ["/var/backups/db"]  
  
# Copy backup script to folder that is used by CRON  
COPY db_backup.sh /etc/periodic/daily/dbbackup  
  
CMD crond -f  

