FROM ubuntu  
RUN apt-get update && apt-get install -y curl  
RUN curl -o /usr/bin/btsync.tar.gz http://download-
new.utorrent.com/endpoint/btsync/os/linux-x64/track/stable  
RUN cd /usr/bin && tar -xzvf btsync.tar.gz && rm btsync.tar.gz  
EXPOSE 8888  
EXPOSE 55555  
ENTRYPOINT ["btsync"]  
CMD ["--config", "/data/etc/btsync.conf", "--nodaemon"]  

