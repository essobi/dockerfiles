FROM phusion/baseimage:latest  
  
USER root  
  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y vim curl mysql-
client openssh-client gettext  
  
RUN mkdir /cron  
ADD ./* /cron/  
  
RUN mkdir /etc/cron.minutely && \  
cp /cron/minutely /etc/cron.minutely/minutely && \  
cp /cron/hourly /etc/cron.hourly/hourly && \  
cp /cron/daily /etc/cron.daily/daily && \  
cp /cron/weekly /etc/cron.weekly/weekly && \  
cp /cron/monthly /etc/cron.monthly/monthly && \  
  
chmod +x /etc/cron.minutely/minutely && \  
chmod +x /etc/cron.hourly/hourly && \  
chmod +x /etc/cron.daily/daily && \  
chmod +x /etc/cron.weekly/weekly && \  
chmod +x /etc/cron.monthly/monthly  
  
RUN rm -f /etc/crontab && \  
cp /cron/crontab /etc/crontab  
  
CMD ["/sbin/my_init"]  

