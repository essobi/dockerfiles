FROM mongo:3.4  
RUN apt-get update && \  
apt-get install -y curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
curl -o /usr/local/bin/mantra -L
https://github.com/pugnascotia/mantra/releases/download/0.0.1/mantra && \  
chmod +x /usr/local/bin/mantra  
  
ENV TZ=America/New_York  
  
ENV MONGO_HOST mongo  
ENV BACKUP_DIR dump  
  
ENV CRON_PATTERN='0 0 3 * * *'  
ENV DAYS_TO_RETAIN_BACKUP=14  
VOLUME ["/backups"]  
  
COPY mongobackup.sh /usr/local/bin/  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["mongobackup.sh"]  

