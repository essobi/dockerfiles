FROM rabbitmq:3-management  
  
# backups to Amazon S3  
RUN apt-get update && apt-get install -y s3cmd && apt-get install -y cron &&
rm -rf /var/lib/apt/lists/*  
COPY s3cfg /root/.s3cfg  
  
# entrypoint  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
  
VOLUME /var/lib/rabbitmq/  
  
CMD ["cron","-f"]  

