FROM dartagan/borg-backup  
MAINTAINER William Weiskopf <william@weiskopf.me>  
  
USER root  
COPY crontab /crontab  
  
ENTRYPOINT []  
  
CMD ["sh", "-c", "crontab /crontab && crond -d 0 -f"]  
  

