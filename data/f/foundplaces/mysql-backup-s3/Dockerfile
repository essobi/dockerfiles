FROM alpine:3.1  
MAINTAINER Johannes Schickling "schickling.j@gmail.com"  
ADD install.sh install.sh  
RUN sh install.sh && rm install.sh  
  
ENV MYSQLDUMP_OPTIONS --quote-names --quick --add-drop-table --add-locks
--allow-keywords --disable-keys --extended-insert --single-transaction
--create-options --comments --net_buffer_length=16384  
ENV MYSQLDUMP_DATABASE --all-databases  
ENV MYSQL_HOST **None**  
ENV MYSQL_PORT 3306  
ENV MYSQL_USER **None**  
ENV MYSQL_PASSWORD **None**  
ENV S3_ACCESS_KEY_ID **None**  
ENV S3_SECRET_ACCESS_KEY **None**  
ENV S3_BUCKET **None**  
ENV S3_REGION us-east-1  
ENV S3_PATH 'backup'  
ENV SCHEDULE **None**  
  
ADD run.sh run.sh  
ADD backup.sh backup.sh  
  
CMD ["sh", "run.sh"]  

