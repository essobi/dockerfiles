FROM debian:jessie  
  
  
# entrypoint, snapshotter  
COPY entrypoint.sh /entrypoint.sh  
COPY snapshotter.sh /snapshotter.sh  
  
# backups to Amazon S3  
RUN apt-get update && apt-get install -y s3cmd cron curl && rm -rf
/var/lib/apt/lists/*  
COPY s3cfg /root/.s3cfg  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["cron","-f"]  

