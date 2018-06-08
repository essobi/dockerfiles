FROM postgres  
ENV BACKUP_DIR /usr/backups/  
WORKDIR $BACKUP_DIR  
ADD ./pg_* ${BACKUP_DIR}/  
RUN chmod +x pg_*.sh && chmod +x pg_crontab && ln -s ${BACKUP_DIR}/pg_crontab
/etc/cron.d && touch /var/log/cron.log  
VOLUME $BACKUP_DIR/postgresql/  
CMD cron && tail -f /var/log/cron.log  

