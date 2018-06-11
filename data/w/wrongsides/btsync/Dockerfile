FROM wrongsides/baseimage  
  
# Doownload and extract the executable  
ADD https://download-cdn.getsync.com/stable/linux-x64/BitTorrent-
Sync_x64.tar.gz /btsync.tar.gz  
RUN tar -xzvf btsync.tar.gz && rm btsync.tar.gz  
  
# Web GUI  
EXPOSE 8888  
# Listening port  
EXPOSE 55555  
USER jarvis  
  
ENTRYPOINT ["/btsync"]  
CMD ["--config", "/config/btsync.conf", "--nodaemon"]  

