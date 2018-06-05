FROM arnaudpiroelle/base  
MAINTAINER Arnaud Piroelle  
  
RUN wget -O /opt/btsync.tar.gz https://download-
cdn.getsyncapp.com/stable/linux-x64/BitTorrent-Sync_x64.tar.gz  
  
COPY asset/btsync.conf /opt/btsync.conf  
COPY entrypoint.sh /opt/entrypoint.sh  
  
VOLUME ["/btsync"]  
VOLUME ["/shared"]  
  
EXPOSE 8888  
EXPOSE 55555  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["/btsync/bin/btsync", "--config", "/btsync/config/btsync.conf", "--
nodaemon"]  

