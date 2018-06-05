###  
# Automated Build for dklein/nextcloud Image  
# Version 1.0  
# (c) 2017 Dennis Klein  
#  
FROM nextcloud  
  
# install cron  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y cron && \  
rm -rf /var/lib/apt/lists/*  
  
# install modified entrypoint.sh  
COPY entrypoint.sh /entrypoint.sh  
  
# change shell for www-data to use cron and execute the occ command  
RUN chsh -s /bin/bash www-data  
  
# activate cronjob  
RUN echo '*/15 * * * * /usr/local/bin/php -f /var/www/html/cron.php' >>
/tmp/www-data.crontab && \  
crontab -u www-data /tmp/www-data.crontab && \  
rm /tmp/www-data.crontab  

