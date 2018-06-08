FROM nextcloud:fpm  
  
RUN apt-get update && \  
apt-get install -y supervisor cron && \  
rm -rf /var/lib/apt/lists/*  
  
COPY cronjobs /tmp  
RUN crontab - < /tmp/cronjobs && \  
rm /tmp/cronjobs  
  
RUN mkdir /var/log/supervisord /var/run/supervisord  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]  

