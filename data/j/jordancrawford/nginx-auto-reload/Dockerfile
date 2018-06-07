  
FROM nginx:latest  
  
MAINTAINER Jordan Crawford <jordan@crawford.kiwi>  
  
# Setup cron.  
RUN apt-get update && apt-get install cron -y && apt-get clean  
  
# Setup the cron job.  
RUN echo "0 0 * * * root nginx -s reload" >> /etc/crontab  
  
# Setup cron to automatically re-load the NGINX configuration daily.  
CMD cron && nginx -g "daemon off;"  

