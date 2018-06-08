FROM debian  
  
RUN apt-get clean && apt-get update --fix-missing && apt-get install --no-
install-recommends -y -q \  
clamav \  
clamav-daemon \  
cron  
  
RUN freshclam  
  
# Add crontab file and startup script.  
COPY crontab /etc/cron.d/clamav-scan  
COPY start.sh /start.sh  
  
VOLUME /scan  
  
RUN chmod 0644 /etc/cron.d/clamav-scan  
RUN chmod 755 /start.sh  
RUN touch /var/log/cron.log  
  
CMD /start.sh

