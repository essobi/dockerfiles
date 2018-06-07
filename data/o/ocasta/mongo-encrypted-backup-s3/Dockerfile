# From ubuntu:trusty as mongodb on alpine is fraught  
FROM ubuntu:trusty  
  
MAINTAINER Martin Higham "martin@ocasta.com"  
ADD install.sh install.sh  
RUN sh install.sh && rm install.sh  
  
ENV MONGODUMP_OPTIONS --oplog  
ENV MONGO_HOST **None**  
ENV MONGO_USER **None**  
ENV MONGO_PASSWORD **None**  
ENV S3_ACCESS_KEY_ID **None**  
ENV S3_SECRET_ACCESS_KEY **None**  
ENV S3_BUCKET **None**  
ENV S3_REGION us-west-1  
ENV S3_PATH 'backup'  
ENV SCHEDULE **None**  
  
ADD run.sh run.sh  
ADD backup.sh backup.sh  
  
CMD ["sh", "run.sh"]  

