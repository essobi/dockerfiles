FROM postgres:9.4  
MAINTAINER unknownlighter@gmail.com  
  
COPY pg_backup /pg_backup  
  
COPY crontab /etc/cron.d/  
  
RUN chmod 0644 /etc/cron.d/crontab  
  
COPY cron_task.sh /  
  
RUN touch /var/log/cron.log  
  
VOLUME /backups  
  
CMD env > /root/env.sh && cron && tail -f /var/log/cron.log  

