FROM ubuntu  
  
MAINTAINER Guillame Boddaert <guillaume@lighthouse-analytics.co>  
  
RUN apt-get update && \  
apt-get install mysql-client cron bzip2 -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir /backups  
  
ENV BACKUP_TIME 1 3 * * *  
  
COPY docker-entrypoint.sh /entrypoint.sh  
COPY backup restore /bin/  
  
VOLUME /backups  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["cron", "-f"]  

