FROM prom/alertmanager:master  
  
ENV \  
ARG_COMMAND=/bin/alertmanager \  
ARG_PREFIX=ALERTMGR_ \  
ALERTMGR_STORAGE_PATH=/alertmanager  
  
ADD entrypoint.sh /entrypoint  
ENTRYPOINT [ "/entrypoint" ]  

