FROM alpine:latest  
  
ADD backup.sh /backup.sh  
  
RUN apk update  
RUN apk add rsync openssh  
  
RUN \  
apk update && \  
apk add rsync openssh && \  
rm /var/cache/apk/* && \  
chmod a+x backup.sh  
  
CMD "/backup.sh"  
  

