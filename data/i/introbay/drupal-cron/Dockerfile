FROM introbay/php:7.0-apache  
MAINTAINER ignacio@introbay.com  
  
RUN apt-get update && apt-get install -y cron && \  
rm -r /var/lib/apt/lists/*  
  
# Add crontab file in the cron directory  
ADD crontab /etc/cron.d/drush-cron  
  
# Give execution rights on the cron job  
RUN chmod 0644 /etc/cron.d/drush-cron  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
  
# Run the command on container startup  
ENTRYPOINT []  
CMD cron && tail -f /var/log/cron.log  
  

