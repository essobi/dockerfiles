FROM debian:stretch-slim  
  
ENV habitica_user null  
ENV habitica_token null  
ENV todoist_token null  
  
RUN mkdir -p /root/.config/habitica/ /app/hab_backup /app/hab_scripts  
ADD habitica-scripts /app/hab_scripts  
ADD auth.cfg /app  
ADD check_bosser.sh /app  
ADD start.sh /app  
  
RUN apt-get update && apt-get install -y cron python python-pip curl logrotate
sed  
  
RUN pip install requests habitica  
  
ADD crontab /etc/cron.d/hab_scripts  
ADD logrotate /etc/logrotate.d/hab_scripts  
  
RUN ln -s /app/auth.cfg /root/.config/habitica/auth.cfg  
  
RUN crontab /etc/cron.d/hab_scripts  
  
CMD ["/app/start.sh"]  

