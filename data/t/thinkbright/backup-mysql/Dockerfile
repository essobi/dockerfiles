FROM alpine:latest  
LABEL \  
nl.thinkbright.docker-mysql-backup.author = "jacco@thinkbright.nl" \  
nl.thinkbright.docker-mysql-backup.version = "1.0"  
  
# Copy usr-local-bin into container  
COPY ./usr-local-bin/ /usr/local/bin/  
  
ENV BACKUP_MYSQLDUMP_OPTIONS --quote-names --quick --add-drop-table --add-
locks --allow-keywords --disable-keys --extended-insert --single-transaction
--create-options --comments --net_buffer_length=16384  
ENV BACKUP_MYSQL_DATABASE **None**  
ENV BACKUP_MYSQL_HOST **None**  
ENV BACKUP_MYSQL_PORT 3306  
ENV BACKUP_MYSQL_USER **None**  
ENV BACKUP_MYSQL_PASSWORD **None**  
ENV BACKUP_MYSQL_PASSWORD_FILE **None**  
  
ENV BACKUP_S3_ACCESS_KEY_ID **None**  
ENV BACKUP_S3_SECRET_ACCESS_KEY **None**  
ENV BACKUP_S3_BUCKET **None**  
ENV BACKUP_S3_PREFIX **None**  
ENV BACKUP_S3_REGION eu-west-1  
ENV BACKUP_S3_ENDPOINT **None**  
ENV BACKUP_S3_S3V4 no  
ENV BACKUP_S3_PREFIX backup  
ENV BACKUP_S3_ACCESS_KEY_ID_FILE **None**  
ENV BACKUP_S3_SECRET_ACCESS_KEY_FILE **None**  
ENV BACKUP_CRON_ENTRY **None**  
  
RUN install.sh && \  
rm /usr/local/bin/install.sh  
  
CMD tail -f /dev/null  

