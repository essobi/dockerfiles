FROM mysql:5.7  
# Set correct timezone  
RUN echo "Pacific/Auckland" > /etc/timezone  
RUN dpkg-reconfigure --frontend noninteractive tzdata  
  
# Install and setup cron  
RUN apt-get update && apt-get install -y cron  
ADD crontab /crontab  
RUN /usr/bin/crontab /crontab  
RUN mkdir /var/log/cron  
  
# Install and setup supervisord  
RUN apt-get update && apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
COPY supervisord.conf /etc/supervisor/supervisord.conf  
  
# Copy backup script  
ADD db-backup.sh /db-backup.sh  
RUN chmod +x /db-backup.sh  
  
# Reset ENTRYPOINT because we are starting mysql with supervisord,  
# not the ENTRYPOINT and CMD from the mysql docker container  
ENTRYPOINT []  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

