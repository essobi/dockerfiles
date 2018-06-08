FROM alpine  
  
ENV LOGROTATE_PATHS /var/log/*.log  
ENV LOGROTATE_OPTIONS rotate 72, dateext, dateformat -%Y%m%d_%H%M%S, compress,
missingok, notifempty, nocreate, su root root  
ENV LOGROTATE_CONFIG /etc/logrotate.conf  
  
RUN \  
apk update && \  
apk add logrotate && \  
rm -rf /var/cache/apk  
  
ADD start /start  
  
USER root  
  
ENTRYPOINT ["/start"]  

