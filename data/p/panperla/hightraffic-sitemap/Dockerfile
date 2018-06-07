# Crontab running sitemap generation based on redis entries  
FROM ubuntu:latest  
MAINTAINER mp@meant4.com  
RUN apt-get update && apt-get install cron redis-tools gawk -y  
  
# Add crontab file in the cron directory  
ADD crontab /etc/cron.d/sitemap-cron  
ADD sitemaps /usr/sbin/sitemaps  
ADD xmlsitemap /usr/sbin/xmlsitemap  
RUN chmod +x /usr/sbin/sitemaps  
RUN chmod +x /usr/sbin/xmlsitemap  
  
# Give execution rights on the cron job  
RUN chmod 0644 /etc/cron.d/sitemap-cron  
  
# Create the log file to be able to run tail  
RUN touch /var/log/cron.log  
  
# Run the command on container startup  
CMD cron && tail -f /var/log/cron.log

