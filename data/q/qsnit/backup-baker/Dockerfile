FROM alpine:latest  
  
ADD install.sh install.sh  
RUN sh install.sh && rm install.sh  
  
RUN mkdir /data  
RUN mkdir /backup  
  
WORKDIR /data  
  
#Local backup\retention enviroments setup  
ENV DPATH /backup  
ENV SPATH /data  
ENV RETENTION 10  
ENV RETENTION_DEPTH 32  
ENV SCHEDULE null  
  
#AWS S3 enviroments setup  
ENV S3_ACCESS_KEY_ID null  
ENV S3_SECRET_ACCESS_KEY null  
ENV S3_BUCKET null  
ENV S3_REGION us-east-1  
ENV S3_ENDPOINT null  
ENV S3_S3V4 no  
  
#AWS S3 bucket path prefixes  
ENV S3_FILES_PREFIX 'file_backup'  
ENV S3_DB_PREFIX 'sql_backup'  
ADD run.sh /usr/share/run.sh  
ADD backup.sh /usr/share/backup.sh  
ADD rotate.sh /usr/share/rotate.sh  
  
CMD ["sh", "/usr/share/run.sh"]  

