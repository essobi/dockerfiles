FROM alpine:3.7  
RUN apk --update add \  
inotify-tools \  
unrar \  
bash  
  
# where to check  
VOLUME [ "/watch" ]  
  
COPY ./monitor.sh /app/  
ENTRYPOINT [ "/app/monitor.sh" ]  

