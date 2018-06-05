  
FROM bender77/debianbase  
  
RUN apt-get update && apt-get install curl -y  
RUN curl
http://download.getsyncapp.com/endpoint/btsync/os/linux-x64/track/stable >
btsync.tgz  
RUN tar -xf btsync.tgz  
  
VOLUME ["/data"]  
EXPOSE 8888  
CMD /btsync --nodaemon --webui.listen 0.0.0.0:8888  

