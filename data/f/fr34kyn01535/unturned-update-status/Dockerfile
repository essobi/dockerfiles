FROM ubuntu:latest  
  
RUN apt update && apt -y install cron nginx pcregrep curl lib32gcc1  
  
ADD crontab /etc/cron.d/update  
ADD update.sh /root/update.sh  
RUN mkdir -p /root &&\  
cd /root &&\  
curl -s http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar
-vxz  
  
RUN chmod 644 /etc/cron.d/update  
RUN chmod 777 /root/update.sh  
RUN touch /var/log/cron.log  
RUN echo "Running initial update..." > /var/www/html/index.html  
WORKDIR /root  
  
CMD service nginx start && service cron start && tail -f /var/log/cron.log

