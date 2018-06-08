FROM debian:latest  
  
RUN apt-get update \  
&& apt-get install -y cron tar mariadb-client \  
&& apt-get autoclean \  
&& rm -rf /var/lib/apt/lists/* \  
&& touch /var/log/cron.log  
  
COPY backup_cron.sh /backup_cron.sh  
COPY variables /variables  
COPY docker-entrypoint.sh /entrypoint.sh  
  
RUN chmod +x /backup_cron.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD cron && tail -f /var/log/cron.log  

