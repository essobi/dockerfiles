FROM nginx:latest  
  
MAINTAINER yang.leijun@gmail.com  
  
RUN apt-get update && apt-get -y -q install logrotate supervisor cron  
RUN mkdir -p /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY logrotate.conf /etc/logrotate.d/nginx  
RUN chmod 644 /etc/logrotate.d/nginx  
  
#Copy daily logrotate script to hourly  
RUN cp /etc/cron.daily/logrotate /etc/cron.hourly/  
  
# Define default command.  
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

