FROM ubuntu:14.04  
# BtSync Installation  
ENV SECRET false  
WORKDIR /usr/local/bin  
  
ADD http://download-new.utorrent.com/endpoint/btsync/os/linux-x64/track/stable
/usr/local/bin/btsync.tar.gz  
  
RUN \  
tar -zxf btsync.tar.gz && rm btsync.tar.gz; \  
chown root: /usr/local/bin -R && chmod 755 btsync; \  
mkdir -p /btsync/.sync /var/run/btsync /data  
  
ADD build/btsync.conf /btsync/btsync.conf  
ADD build/btsync.sh /btsync/run  
  
RUN chmod +x /btsync/run  
  
EXPOSE 8888 55555  
VOLUME ["/data"]  
CMD ["/btsync/run"]  
# End BtSync  

