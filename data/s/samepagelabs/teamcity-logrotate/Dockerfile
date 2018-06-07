FROM samepagelabs/logrotate  
  
ENV LOGROTATE_PATHS /opt/TeamCity/logs/catalina.out  
ENV LOGROTATE_OPTIONS rotate 72, dateext, dateformat -%Y%m%d_%H%M%S, compress,
missingok, notifempty, nocreate, copytruncate, su root root  

