  
FROM ubuntu:14.04  
MAINTAINER Axisto Media  
  
RUN apt-get update --fix-missing  
RUN apt-get install -y mongodb-clients openssl curl  
  
ADD ./backup.sh /mongodb-s3-backup/backup.sh  
WORKDIR /mongodb-s3-backup  
RUN chmod +x /mongodb-s3-backup/backup.sh  
  
ENTRYPOINT ./backup.sh  

