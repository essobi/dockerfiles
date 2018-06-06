FROM alpine:latest  
LABEL maintainer="Steve Griffiths <sgriffiths@cirrus1.net>"  
  
ADD install.sh install.sh  
RUN sh install.sh && rm install.sh  
  
ENV MYSQLDUMP_OPTIONS --quote-names --quick --add-drop-table --add-locks
--allow-keywords --disable-keys --extended-insert --single-transaction
--create-options --comments --net_buffer_length=16384  
ENV MYSQLDUMP_DATABASE --all-databases  
ENV MYSQL_SERVICE_HOST **None**  
ENV MYSQL_SERVICE_PORT 3306  
ENV MYSQL_USER **None**  
ENV MYSQL_PASSWORD **None**  
ENV S3_ACCESS_KEY_ID **None**  
ENV S3_SECRET_ACCESS_KEY **None**  
ENV S3_BUCKET **None**  
ENV S3_REGION us-west-1  
ENV S3_ENDPOINT **None**  
ENV S3_S3V4 no  
ENV S3_PREFIX 'backup'  
ENV MULTI_FILES no  
ENV SCHEDULE **None**  
  
ADD run.sh run.sh  
ADD backup.sh backup.sh  
  
CMD ["sh", "run.sh"]  

