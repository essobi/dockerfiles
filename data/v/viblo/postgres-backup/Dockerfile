FROM alpine:latest  
  
ARG BACKUP_USER=root  
ENV HOSTNAME=postgres  
ENV USERNAME=postgres  
ENV PGPASSWORD=postgres  
ENV BACKUP_DIR=/data  
ENV SCHEMA_ONLY_LIST=""  
ENV ENABLE_CUSTOM_BACKUPS=yes  
ENV ENABLE_PLAIN_BACKUPS=no  
ENV ENABLE_GLOBALS_BACKUPS=no  
ENV DAY_OF_WEEK_TO_KEEP=5  
ENV DAYS_TO_KEEP=7  
ENV WEEKS_TO_KEEP=5  
ENV CRON_EXPRESSION="0 4 * * *"  
RUN apk add \--update --no-cache postgresql-client  
  
VOLUME /data  
  
ADD pg_backup.sh /usr/local/bin/pg_backup  
ADD pg_backup_rotated.sh /usr/local/bin/pg_backup_rotated  
  
RUN echo "$CRON_EXPRESSION pg_backup_rotated" >
/var/spool/cron/crontabs/$BACKUP_USER  
  
USER $BACKUP_USER  
  
CMD ["crond", "-l2", "-f"]  

