FROM alpine:3.7  
RUN apk --no-cache add bash rsync inotify-tools  
  
RUN mkdir /rookfs  
RUN mkdir /rookfs-rsync-backup  
  
WORKDIR /rookfs  
  
ENTRYPOINT ["tail", "-f", "/dev/null"]  

