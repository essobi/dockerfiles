FROM postgres:9.6.3-alpine  
MAINTAINER Josh Friend <jfriend@michiganlabs.com>  
  
# Install backup schedule  
COPY crontabs /var/spool/cron/crontabs  
COPY backup_databases.sh /  
  
CMD crond -d 6 -f  

