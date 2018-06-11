FROM jrottenberg/ffmpeg:3.3  
MAINTAINER rubenmch  
  
COPY watcher /usr/bin/watcher  
  
RUN ["chmod", "+x", "/usr/bin/watcher"]  
  
RUN apt-get update  
  
RUN apt-get install -y inotify-tools  
  
ENTRYPOINT ["/usr/bin/watcher"]  

