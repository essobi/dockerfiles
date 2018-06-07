FROM alpine  
  
RUN apk add ca-certificates bash duplicity --update  
  
ADD backup.sh /backup.sh  
  
CMD /bin/bash /backup.sh  

