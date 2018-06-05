FROM python:3.6-alpine3.6  
LABEL maintainer="Open Knowledge International <sysadmin@okfn.org>"  
  
WORKDIR /app  
VOLUME /app  
  
COPY docker/crontab /var/spool/cron/crontabs/root  
COPY update_status.py /usr/bin/update_status  
  
RUN chmod +x /usr/bin/update_status  
  
ENTRYPOINT ["/usr/sbin/crond", "-d", "6", "-f"]  

