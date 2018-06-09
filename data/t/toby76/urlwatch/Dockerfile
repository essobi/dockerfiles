FROM debian:buster  
  
RUN apt-get update && apt-get install -y urlwatch python3-pip cron  
RUN python3 -m pip install --upgrade pip  
RUN python3 -m pip install pyyaml minidb requests keyring appdirs  
WORKDIR /root  
  
COPY crontab /etc/cron.d/crontab  
  
CMD urlwatch  
  
VOLUME /root  
  
CMD ["cron", "-f"]  

