FROM zadara/ssh:alpine  
ENV SSH_SERVER="disabled"  
LABEL description="Basic cron service derived from the ssh container"  
  
ENV CRON_SERVICE="enabled"  
# CRON_DIR="/etc/cron.d"  
RUN mkdir /etc/periodic/5min /etc/periodic/10min && \  
echo "*/5 * * * * run-parts /etc/periodic/5min" >>
/var/spool/cron/crontabs/root && \  
echo "*/10 * * * * run-parts /etc/periodic/10min" >>
/var/spool/cron/crontabs/root  

