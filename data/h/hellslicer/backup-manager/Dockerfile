FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y --no-install-recommends cron backup-
manager && apt-get clean && rm -rf /var/cache/apt/* /var/lib/apt/lists/*  
  
RUN echo "0 4 * * * /usr/sbin/backup-manager" > cron && crontab cron && rm
cron  
  
RUN touch /var/log/cron.log  
  
CMD cron && tail -f /var/log/cron.log  

